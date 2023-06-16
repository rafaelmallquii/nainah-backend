function getElementByXpath(path) {
    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

// window.addEventListener('DOMContentLoaded', function() {
//     var copyBtn = document.getElementById('copyValues');
    
//     if (copyBtn) {
//         copyBtn.addEventListener('click', function() {
//             var copyFrom = getElementByXpath('//*[@id="id_title"]');
//             var copyTo = getElementByXpath('//input[contains(@id,"title") and contains(@class,"my-title-input")]');
//             copyTo.value = copyFrom.value;
//         });
//     }
// });