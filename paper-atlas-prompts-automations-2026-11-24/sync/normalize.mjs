export function cleanText(value) {
  if (typeof value !== 'string') return null
  const cleaned = value.replace(/-\s*\n\s*/g, '').replace(/\s+/g, ' ').trim()
  return cleaned || null
}

export function extractArxivId(...values) {
  const text = values.filter(Boolean).join(' ')
  const match = text.match(/(?:arxiv(?:\.org\/abs\/|:)?\s*)?\b(\d{4}\.\d{4,5})(v\d+)?\b/i)
  return match ? { id: match[1], version: match[2] ?? null } : null
}

export function normalizeTitle(value) {
  return cleanText(value)?.toLocaleLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ') ?? ''
}

export function canonicalKey(record) {
  const arxiv = extractArxivId(record.arxiv_id, record.source_url, record.title)
  if (arxiv) return `arxiv:${arxiv.id}`
  if (record.doi) return `doi:${record.doi.toLocaleLowerCase().replace(/^https?:\/\/(?:dx\.)?doi\.org\//, '')}`
  const title = normalizeTitle(record.paper_title || record.title)
  const firstAuthor = normalizeTitle(record.authors?.[0] || '')
  return `title:${title}${firstAuthor ? `:${firstAuthor}` : ''}`
}

export function validSourceUrl(record) {
  const arxiv = extractArxivId(record.arxiv_id)
  return arxiv ? `https://arxiv.org/abs/${arxiv.id}` : null
}

export function normalizeRecord(raw, source) {
  const title = cleanText(raw.paper_title || raw.title || raw.display_title_raw)
  if (!title) throw new Error('论文标题为空')
  const arxiv = extractArxivId(raw.arxiv_id, raw.source_url, raw.introduction, title)
  const normalized = {
    canonical_key: canonicalKey({ ...raw, title }),
    title,
    chinese_title: cleanText(raw.chinese_title),
    authors: Array.isArray(raw.authors) ? raw.authors.map(cleanText).filter(Boolean) : [],
    affiliations: Array.isArray(raw.affiliations) ? raw.affiliations.map(cleanText).filter(Boolean) : [],
    arxiv_id: arxiv?.id ?? null,
    paper_date: cleanText(raw.paper_date),
    paper_date_precision: raw.paper_date_precision || 'unknown',
    primary_ingest_time: raw.ingest_time || raw.primary_ingest_time || null,
    source_abstract: cleanText(raw.source_abstract),
    chinese_abstract: cleanText(raw.chinese_abstract),
    chinese_content_kind: raw.chinese_abstract ? (raw.chinese_content_kind || 'AI 摘要') : null,
    tags: Array.isArray(raw.tags) ? [...new Set(raw.tags.map(cleanText).filter(Boolean))] : [],
    evidence_tags: Array.isArray(raw.evidence_tags) ? [...new Set(raw.evidence_tags.map(cleanText).filter(Boolean))] : [],
    kb_names: [source.displayName],
    primary_detail_url: `https://ima.qq.com/wiki/?shareId=${source.shareId}${raw.media_id ? `&mediaId=${encodeURIComponent(raw.media_id)}&action=openDetailDrawer` : ''}`,
    source_url: validSourceUrl({ arxiv_id: arxiv?.id }),
    parse_status: raw.source_abstract && raw.authors?.length ? 'ready' : 'partial',
  }
  return normalized
}

export function dedupeRecords(records) {
  const map = new Map()
  for (const record of records) {
    const current = map.get(record.canonical_key)
    if (!current) {
      map.set(record.canonical_key, record)
      continue
    }
    map.set(record.canonical_key, {
      ...current,
      ...Object.fromEntries(Object.entries(record).filter(([, value]) => value !== null && value !== undefined && (!Array.isArray(value) || value.length > 0))),
      kb_names: [...new Set([...(current.kb_names || []), ...(record.kb_names || [])])],
      authors: current.authors?.length ? current.authors : record.authors,
      affiliations: [...new Set([...(current.affiliations || []), ...(record.affiliations || [])])],
      source_abstract: current.source_abstract || record.source_abstract,
      chinese_abstract: current.chinese_abstract || record.chinese_abstract,
    })
  }
  return [...map.values()]
}
