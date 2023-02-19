const colors = {
  red: '#bf616a',
  orange: '#d08770',
  yellow: '#ebcb8b',
  green: '#a3be8c',
  blue: '#81a1c1',
  purple: '#b48ead',
  black: '#2e3440',
  darkest: '#3b4252',
  darker: '#434c5e',
  dark: '#4c566a',
  medium: '#767f90',
  light: '#d8dee9',
  lighter: '#e5e9f0',
  lightest: '#eceff4',
} as const

export default colors

export function rgb(hex: string) {
  const r = parseInt(hex.slice(1, 3), 16)
  const g = parseInt(hex.slice(3, 5), 16)
  const b = parseInt(hex.slice(5, 7), 16)
  return [r, g, b] as const
}
