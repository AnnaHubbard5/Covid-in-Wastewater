import { format as formatDate } from 'date-fns'

const fmtDate = (date: string | Date) => formatDate(new Date(date), 'MMM d, y')

export default async function getCases() {
  const res = await fetch('/cases.csv')
  let csv = (await res.text()).split('\n')

  // Convert csv to json
  csv = csv.slice(1)
  let cases: {
    [county: string]: {
      [date: string]: number
    }
  } = {}

  const dates: string[] = []
  for (let i = 0; i < csv.length; i++) {
    const row = csv[i]
    const split = row.split(',')
    const countyName = split[0]
    const state = split[2]
    if (state != 'California') {
      continue
    }
    console.log({ state })
    const date = fmtDate(split[split.length - 1])
    const numCases = split[9]
    if (!(countyName in cases)) {
      cases[countyName] = {}
    }
    if (!(date in dates)) {
      dates.push(date)
    }
    cases[countyName][date] = parseFloat(numCases)
    console.log(i)
  }

  console.log('got dates', dates)
  return cases
}
