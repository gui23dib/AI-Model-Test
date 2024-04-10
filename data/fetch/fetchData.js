function onOpen(e) {
  SpreadsheetApp.getUi().createMenu('SKYFALL')
    .addItem('Update', 'skyfall')
    .addToUi();
}

function skyfall() {
  const ss = SpreadsheetApp.getActiveSpreadsheet()
  const sheet = ss.getSheetByName("BB")
  const range = sheet.getRange(2, 1, sheet.getLastRow() - 1, sheet.getLastColumn())
  range.sort({ column: 1, ascending: false })

  SpreadsheetApp.flush()
  const results = []

  const values = sheet.getRange(2, 1, sheet.getLastRow() - 1, 2).getValues()
  const filter = values.filter(row => row[0] == true)
  const urls = filter.map(row => {
    const url = row[1]
    const cardname = /([^\/]+)$/gm.exec(url)[1]
    return `https://api.scryfall.com/cards/named?fuzzy=${cardname}`
  })

  UrlFetchApp.fetchAll(urls).forEach(req => {
    const data = JSON.parse(req.getContentText())
    results.push([
      data.name,
      data.set_name,
      data.type
      //THE REST
    ])
  })

  sheet.getRange(2, 3, results.length, results[0].length).setValues(results)

}