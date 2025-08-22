
async function growQuote() {
    let quoteElement = document.getElementById("quote-text");

    let size = 14;

    while (size <= 72) {
        size = size + 1;
        quoteElement.style.fontSize = size + "px";

        await new Promise(r => setTimeout(r, 100));
    }
}
