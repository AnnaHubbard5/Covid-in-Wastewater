import { format as formatDate } from 'date-fns'

// const fmtDate = (date: string | Date) => formatDate(new Date(date), 'MMM d, y')
const fmtDate = (date: string | Date) => new Date(date).getTime()

export default async function getCases() {
  const res = await fetch('/new_cases.csv')
  let csv = (await res.text()).split('\n')

  // Convert csv to json
  csv = csv.slice(1)
  let cases: {
    [county: string]: {
      [date: number]: number
    }
  } = {}

  for (let i = 0; i < csv.length; i++) {
    const row = csv[i]
    const split = row.split(',')

    const state = split[2]
    if (state != 'California') continue

    const countyName = split[0]
    const date = fmtDate(split[split.length - 1])
    const numCases = split[9]
    if (!(countyName in cases)) {
      cases[countyName] = {}
    }
    cases[countyName][date] = parseFloat(numCases)
  }

  return cases
}
