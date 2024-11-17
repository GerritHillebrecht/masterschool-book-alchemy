modal = document.getElementById("modal-content")
ai_request_button = document.getElementById("ai-request-btn")

ai_request_button.addEventListener("click", async (e) => {
    try {
        res = await fetch("/api/v1/books/ai");
        res_json = await res.json();

        modal.innerHTML = ""
        modal.appendChild(create_recom_template(res_json))
    }
    catch (e) {
        message = document.createElement("p")
        message.classList = "p-4 text-xs uppercase font-bold tracking-widest text-neutral-700"
        message.textContent = "The API-Quota is exceeded. No more recommendations for this month."

        modal.innerHTML = ""
        modal.appendChild(message)
    }
})

function create_recom_template(book) {
    containerDiv = document.createElement("div flex flex-col items-center")

    cover = document.createElement("img")
    cover.className = "aspect-[9/12] object-contain object-fit mb-4"
    cover.src = book["cover"]
    cover.alt = book["author"]

    title = document.createElement("h5")
    title.className = "text-4xl font-bold text-neutral-900"
    title.textContent = book["title"]

    author = document.createElement("p")
    author.className = "text-neutral-700 text-sm mt-2"
    author.textContent = book["author"]

    excerpt = document.createElement("p")
    excerpt.className = "italic mt-4"
    excerpt.textContent = book["excerpt"]

    containerDiv.appendChild(img)
    containerDiv.appendChild(title)
    containerDiv.appendChild(author)
    containerDiv.appendChild(excerpt)

    return containerDiv
}