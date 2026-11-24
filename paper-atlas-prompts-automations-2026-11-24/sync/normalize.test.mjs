import test from 'node:test'
import assert from 'node:assert/strict'
import { cleanText, extractArxivId, canonicalKey, normalizeRecord, dedupeRecords } from './normalize.mjs'
import { qualityReport } from './quality.mjs'

const source = { displayName: 'Scaling Up', shareId: 'share-example' }

test('清洗 PDF 断行并识别 arXiv 版本', () => {
  assert.equal(cleanText('Cross-\n Field   Interaction'), 'CrossField Interaction')
  assert.deepEqual(extractArxivId('arXiv:2507.15551v3'), { id: '2507.15551', version: 'v3' })
})

test('同一 arXiv 不同版本使用同一 canonical key', () => {
  assert.equal(canonicalKey({ source_url: 'https://arxiv.org/abs/2507.15551v1' }), 'arxiv:2507.15551')
  assert.equal(canonicalKey({ arxiv_id: '2507.15551v3' }), 'arxiv:2507.15551')
})

test('规范化保留来源并生成详情链接', () => {
  const record = normalizeRecord({ title: 'RankMixer', media_id: 'media 1', arxiv_id: '2507.15551', authors: ['Jie Zhu'], source_abstract: 'Abstract' }, source)
  assert.equal(record.canonical_key, 'arxiv:2507.15551')
  assert.equal(record.source_url, 'https://arxiv.org/abs/2507.15551')
  assert.match(record.primary_detail_url, /mediaId=media%201/)
  assert.equal(record.parse_status, 'ready')
})

test('跨库重复合并但保留知识库归属', () => {
  const a = normalizeRecord({ title: 'RankMixer', arxiv_id: '2507.15551', authors: ['Jie Zhu'] }, source)
  const b = normalizeRecord({ title: 'RankMixer', arxiv_id: '2507.15551', source_abstract: 'Abstract' }, { displayName: '推荐系统文献', shareId: 'other' })
  const merged = dedupeRecords([a, b])
  assert.equal(merged.length, 1)
  assert.deepEqual(merged[0].kb_names, ['Scaling Up', '推荐系统文献'])
  assert.equal(merged[0].source_abstract, 'Abstract')
})

test('质量报告不会把缺失字段当作已补全', () => {
  const report = qualityReport([normalizeRecord({ title: 'Only title' }, source)])
  assert.equal(report.total, 1)
  assert.equal(report.completeness.authors, 0)
  assert.equal(report.completeness.sourceAbstract, 0)
})
