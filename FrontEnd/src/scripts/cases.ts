import { format as formatDate } from 'date-fns'

// const fmtDate = (date: string | Date) => formatDate(new Date(date), 'MMM d, y')
const fmtDate = (date: string) => new Date(date).getTime()

export default async function getCases() {
  const res = await fetch('/new_cases.csv')
  let csv = (await res.text()).split('\n')

  // Convert csv to json
  csv = csv.slice(1)
  let cases: {
    [county: string]: {
      date: number
      cases: number
    }[]
  } = {}

  for (let i = 0; i < csv.length; i++) {
    const row = csv[i]
    const split = row.split(',')

    const state = split[2]
    if (state != 'California') continue

    const countyName = split[0]
    console.log(
      split[split.length - 1],
      new Date(split[split.length - 1]).toString()
    )
    if (!(countyName in cases)) {
      cases[countyName] = []
    }
    const date = fmtDate(split[split.length - 1])
    const numCases = split[9]
    cases[countyName].push({ date, cases: parseFloat(numCases) })
  }

  return cases
}
