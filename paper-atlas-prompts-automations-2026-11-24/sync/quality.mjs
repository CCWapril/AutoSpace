export function qualityReport(records) {
  const keys = new Set()
  const duplicates = []
  const issues = []
  for (const record of records) {
    if (keys.has(record.canonical_key)) duplicates.push(record.canonical_key)
    keys.add(record.canonical_key)
    if (!record.title) issues.push({ key: record.canonical_key, issue: 'empty_title' })
    if (record.source_url && !/^https:\/\/arxiv\.org\/abs\/\d{4}\.\d{4,5}$/.test(record.source_url)) {
      issues.push({ key: record.canonical_key, issue: 'invalid_arxiv_url' })
    }
    if (record.paper_date && !/^\d{4}(?:-\d{2}(?:-\d{2})?)?$/.test(record.paper_date)) {
      issues.push({ key: record.canonical_key, issue: 'invalid_paper_date' })
    }
  }
  const completeness = (field) => records.filter((record) => {
    const value = record[field]
    return Array.isArray(value) ? value.length > 0 : Boolean(value)
  }).length
  return {
    total: records.length,
    uniqueCanonicalKeys: keys.size,
    duplicates,
    issues,
    completeness: {
      authors: completeness('authors'),
      affiliations: completeness('affiliations'),
      sourceAbstract: completeness('source_abstract'),
      chineseAbstract: completeness('chinese_abstract'),
      paperDate: completeness('paper_date'),
      arxivId: completeness('arxiv_id'),
    },
  }
}
