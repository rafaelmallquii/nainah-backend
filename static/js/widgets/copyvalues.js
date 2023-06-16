function getElementsByXpath(xpath, parent) {
    let results = [];
    let query = document.evaluate(xpath, parent || document,
        null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
    for (let i = 0, length = query.snapshotLength; i < length; ++i) {
        results.push(query.snapshotItem(i));
    }
    return results;
  }

window.addEventListener('load', function() {
    const copyTitleFather = getElementsByXpath('//*[@id="id_title"]');

    const inlinesElements = getElementsByXpath('//input[contains(@id,"title") and contains(@class,"my-title-input")]')

    // copiar copyTitleFather para todos los inlines menos el ultimo
    for (let i = 0; i < inlinesElements.length - 1; i++) {
        // verificar si el inline tiene valor en el titulo para no sobreescribirlo
        if (inlinesElements[i].value == '')

            inlinesElements[i].value = copyTitleFather[0].value;
    }
});