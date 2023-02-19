export default async function getWasteWater() {
  const res = await fetch('/cal-wastewater.csv')
  let csv = (await res.text()).split('\n')

  // Convert csv to json
  csv = csv.slice(1)
  let waterQualities: {
    [county: string]: {
      [plantId: string]: {
        [date: string]: number
      }
    }
  } = {}

  const dates: string[] = []
  for (let i = 0; i < csv.length; i++) {
    const row = csv[i]
    const split = row.split(',')
    const countyName = split[6]
    const date = split[9]
    const percentile = split[13]
    const plantId = split[1]
    if (!(date in dates)) {
      dates.push(date)
    }
    if (!(countyName in waterQualities)) {
      waterQualities[countyName] = {}
    }
    if (!(plantId in waterQualities[countyName])) {
      waterQualities[countyName][plantId] = {}
    }
    waterQualities[countyName][plantId][date] = parseFloat(percentile)
  }

  return waterQualities
}
