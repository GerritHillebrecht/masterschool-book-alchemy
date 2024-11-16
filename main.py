import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from sqlalchemy import desc, asc

from data_models import db, Author, Book

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data", "library.sqlite")}'
CORS(app, resources={r"/api/*": {"origins": "*"}})

db.init_app(app)


@app.get("/api/v1/populate")
def get_populate_database():
    populate_database()

    return jsonify([
        book.to_dict()
        for book in db.session.query(Book).join(Author).all()
    ])


@app.get("/")
def get_home():
    sort_by = request.args.get("sort_by", "id")
    sort_order = request.args.get("sort_order", "desc")

    if sort_by == "author":
        sort_by_clause = desc(Author.name) if sort_order == "desc" else asc(Author.name)
    else:
        sort_by_clause = desc(sort_by) if sort_order == "desc" else asc(sort_by)

    books = [
        book.to_dict()
        for book in db.session.query(Book)
        .join(Author)
        .order_by(sort_by_clause)
        .all()
    ]
    return render_template("home.html", books=books), 200


@app.get("/api/v1/authors")
def get_authors():
    return jsonify([
        author.to_dict()
        for author in db.session.query(Author).join(Book).order_by(Author.id.desc()).all()
    ]), 200


@app.post("/api/v1/authors")
def add_author():
    body = request.json
    if not body:
        return jsonify({
            "message": "No valid data was submitted"
        }), 422

    author = Author(
        name=body.get("name"),
        birth_date=body.get("birth_date"),
        date_of_death=body.get("date_of_death")
    )

    db.session.add(author)
    db.session.commit()

    return jsonify(author.to_dict()), 200


@app.get("/book/<int:book_id>")
def get_book_by_id(book_id: int):
    book = db.session.query(Book).filter(Book.id == book_id).one()
    return render_template("book_detail.html", book=book)


@app.get("/api/v1/books")
def get_books():
    return jsonify([
        book.to_dict()
        for book in db.session.query(Book).join(Author).all()
    ])


@app.get("/api/v1/books/search")
def get_books_by_search():
    search_string = request.args.get("q", "")
    query = db.session.query(Book).join(Author)

    if search_string:
        query = query.filter(
            (Book.title.ilike(f"%{search_string}%")) |
            (Author.name.ilike(f"%{search_string}%"))
        )

    return jsonify([
        book.to_dict()
        for book in query.all()
    ])


@app.post("/api/v1/books")
def add_book():
    body = request.json

    if not body:
        return jsonify({
            "message": "No valid data was submitted"
        }), 422

    book = Book(
        title=body.get("title"),
        isbn=body.get("isbn"),
        author_id=body.get("author_id"),
        publication_year=body.get("publication_year")
    )

    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 200


@app.delete("/api/v1/books/<int:book_id>")
def delete_book(book_id: int):
    db.session.query(Book).filter(Book.id == book_id).delete()
    db.session.commit()

    return jsonify({
        "message": f'Successfully deleted book with id {book_id}'
    })


def populate_database():
    authors = [
        Author(
            name="Franz Kafka",
            image="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Franz_Kafka%2C_1923.jpg/440px-Franz_Kafka%2C_1923.jpg",
            birth_date="1883-07-03",
            date_of_death="1924-06-03"
        ),
        Author(
            name="Oscar Wilde",
            image="https://149886463.v2.pressablecdn.com/wp-content/uploads/2020/10/Oscar-Wilde-2.jpg",
            birth_date="1854-10-16",
            date_of_death="1900-11-30"
        ),
        Author(
            name="Stephen King",
            image="https://img.aachener-zeitung.de/public/lokales/f1u5oq-file7wg6epqwepu7rx3k9g1/alternates/BASE_SIXTEEN_NINE/file7wg6epqwepu7rx3k9g1",
            birth_date="1947-09-21"
        ),
        Author(
            name="Charles Dickens",
            image="https://victorianweb.org/art/illustration/eytinge/141.jpg",
            birth_date="1812-02-07",
            date_of_death="1870-06-09"
        ),
        Author(
            name="Hermann Hesse",
            image="https://library.ethz.ch/en/locations-and-media/platforms/short-portraits/hermann-hesse--1877-1962-/_jcr_content/par/textimage/image.imageformat.textdouble.566772422.jpg",
            birth_date="1877-07-02",
            date_of_death="1962-08-09"
        )
    ]

    books = [
        Book(
            title="Die Verwandlung",
            isbn="9786589008231",
            cover="https://images.thalia.media/00/-/673e270eaeaa46979eedfb6801e2517b/die-verwandlung-taschenbuch-franz-kafka.jpeg",
            excerpt="""
            "The Metamorphosis" is a novella by Franz Kafka, first published in 1915. The story follows Gregor Samsa, a traveling salesman, who wakes up one morning to find himself transformed into a giant insect. This inexplicable transformation is the starting point for a series of increasingly alienating and tragic events.

Gregor’s initial reaction to his transformation is one of denial and practicality. He worries more about being late for work than the fact that he has become an insect. This reflects his dehumanized existence, where his self-worth is tied to his ability to work and support his family. Despite his horrifying new form, Gregor attempts to adjust to his situation and maintain his role as the family's breadwinner.

Gregor’s family, consisting of his parents and his sister, Grete, reacts with shock and horror. They become increasingly repelled by his appearance and behavior. As Gregor becomes more insect-like in his habits and preferences, such as his taste for rotten food and his new mode of movement, his human connections begin to disintegrate. His family isolates him in his room and only interacts with him to provide minimal care. Grete, initially sympathetic, gradually becomes resentful and calls him a burden.

The family’s treatment of Gregor reflects their shifting dynamics and growing estrangement. Financial pressures and the social stigma of Gregor’s condition push them into a state of desperation. Mr. Samsa, once weak and lethargic, becomes aggressive and authoritarian, taking up a job and asserting control over the household. Mrs. Samsa, who is frail and emotional, withdraws and often faints in the presence of Gregor.

As Gregor's condition deteriorates, the family's transformation is evident. They begin to take pride in their self-sufficiency and societal conformity. Gregor’s alienation reaches its peak when the family decides they can no longer tolerate his presence. In a climactic moment, Grete declares that they must get rid of him, a sentiment that the others silently agree with. Overwhelmed by grief and guilt, Gregor retreats to his room and dies alone.

In the aftermath of Gregor's death, the family experiences a sense of relief and renewal. They plan to move to a smaller apartment and find new opportunities, symbolizing their rebirth after the burden of Gregor’s existence is lifted. The story ends on a note of ambiguous hope, with Grete blossoming into a young woman and the family looking forward to a better future.

"The Metamorphosis" is a powerful exploration of themes such as alienation, identity, and the human condition. It delves into the absurdity of life and the fragile nature of human relationships, leaving a profound impact on readers.
""",
            author_id=1,
            publication_year=1915
        ),
        Book(
            title="Das Bildnis des Dorian Gray",
            isbn="9786555980004",
            cover="https://media.suhrkamp.de/mediadelivery/rendition/9ef9d700820c4b6d8f8f32ade0eddb0e/-S400/das-bildnis-des-dorian-gray_9783458360841_cover.jpg",
            excerpt="""
            "The Picture of Dorian Gray," published in 1890, is a philosophical novel by Oscar Wilde. The story explores themes of aestheticism, moral corruption, and the consequences of a hedonistic lifestyle. It follows the life of a handsome young man named Dorian Gray and his gradual descent into moral decay.

The novel begins with Dorian Gray having his portrait painted by the artist Basil Hallward. Basil is fascinated by Dorian's beauty and believes it has inspired his best work. During a visit to Basil's studio, Dorian meets Lord Henry Wotton, a charismatic and cynical nobleman who espouses a philosophy of indulgent hedonism. Lord Henry's influence profoundly affects Dorian, and he becomes obsessed with the idea of preserving his youth and beauty.

Dorian makes a wish that he could remain young and beautiful forever while his portrait ages instead of him. Mysteriously, his wish is granted. As Dorian embarks on a life of indulgence and vice, he remains youthful and unmarred by time, while his portrait becomes increasingly hideous, reflecting the corruption of his soul.

Dorian's descent into debauchery leads to numerous tragic events. He becomes romantically involved with an actress named Sibyl Vane, but ends their relationship cruelly, which drives her to suicide. This marks the beginning of his unfeeling and destructive behavior. Over the years, Dorian engages in various immoral activities, leading to the ruin of many around him, all the while maintaining his outward appearance of innocence and beauty.

Despite his outward charm, Dorian is haunted by the grotesque transformation of his portrait, which he keeps hidden away in a locked room. His conscience is intermittently pricked by the suffering he has caused, but he is unable to change his ways. Eventually, the weight of his guilt becomes unbearable.

In a final act of desperation, Dorian decides to destroy the portrait, believing it will free him from the burden of his sins. He stabs the painting with a knife, but in doing so, he inadvertently kills himself. The servants find his lifeless body, now aged and withered, with the portrait restored to its original, youthful form.

"The Picture of Dorian Gray" is a poignant critique of the superficial values and moral consequences of a life devoted solely to pleasure. Wilde's novel remains a timeless reflection on the dangers of vanity and the pursuit of eternal youth.
            """,
            author_id=2,
            publication_year=1915
        ),
        Book(
            title="Es",
            isbn="9783453435773",
            cover="https://images.thalia.media/00/-/671c6d7bf8c84e0d8429534d2997d6cc/es-epub-stephen-king.jpeg",
            excerpt="""
            "It," published in 1986, is a horror novel by Stephen King. The story unfolds in the fictional town of Derry, Maine, and follows a group of children who call themselves "The Losers' Club." The novel alternates between two timelines: the late 1950s, when the protagonists are children, and the mid-1980s, when they are adults.

The novel begins with a chilling incident in 1957, when a young boy named George Denbrough is gruesomely murdered by a malevolent entity that often takes the form of a clown named Pennywise. George's older brother, Bill, devastated by his loss, becomes determined to confront the evil force. He gathers his friends—Ben, Beverly, Eddie, Richie, Mike, and Stan—each of whom has encountered the sinister presence of "It."

As children, the group discovers that "It" is an ancient, shape-shifting entity that awakens every 27 years to feed on the town's children. The Losers' Club confronts their deepest fears, manifested by "It," and realizes they must band together to have any chance of defeating it. They venture into the sewers, where they confront Pennywise and inflict what they believe to be a mortal wound, promising to reunite if the creature ever returns.

Twenty-seven years later, "It" resurfaces, and the now-adult members of The Losers' Club are called back to Derry by Mike, the only one who remained in town. Despite the passage of time and the onset of amnesia about their childhood battle, they honor their promise and return, rekindling their old bonds and piecing together their fragmented memories.

As adults, they must face not only the revived horror of "It" but also their own personal traumas and unresolved issues. The story delves deeply into themes of friendship, memory, and the power of childhood resilience. The Losers' Club's final confrontation with "It" takes them back to the sewers, where they must overcome their fears once more.

In the climactic battle, they discover that the true form of "It" is a monstrous spider-like creature. Through their combined courage and unwavering friendship, they manage to defeat "It" and destroy its physical form, breaking the cycle of terror that has plagued Derry for centuries.

"It" is a compelling tale of horror that explores the power of fear and the enduring strength of friendship. With its rich character development and interwoven timelines, the novel showcases Stephen King's mastery of storytelling, leaving a lasting impact on readers.
            """,
            author_id=3,
            publication_year=1986
        ),
        Book(
            title="Oliver Twist",
            isbn="9780786177899",
            cover="https://m.media-amazon.com/images/I/51FaJeXVkmL._SY445_SX342_.jpg",
            excerpt="""
            "Oliver Twist," published in 1837-1839, is one of Charles Dickens's most famous novels. It tells the story of a young orphan, Oliver Twist, who is born in a workhouse and faces a harsh and unforgiving world.

The novel opens with Oliver's birth in a workhouse in a small town in England. His mother dies shortly after his birth, leaving him an orphan. He grows up in the workhouse, where he experiences mistreatment and neglect. At the age of nine, Oliver is transferred to a branch workhouse, where he endures further abuse. One day, after receiving a meager meal, Oliver daringly asks for more food, which leads to him being punished and sold into apprenticeship to an undertaker, Mr. Sowerberry.

Oliver's life with the Sowerberrys is equally harsh, and he eventually runs away to London. In London, he meets Jack Dawkins, also known as the Artful Dodger, who introduces him to Fagin, a career criminal who runs a gang of child thieves. Unaware of their criminal activities, Oliver is taken in by Fagin and the gang. He soon realizes their true nature but feels trapped in his circumstances.

During a pickpocketing expedition, Oliver is caught but later acquitted thanks to the testimony of the victim, Mr. Brownlow, who takes Oliver into his care. Oliver experiences kindness and compassion for the first time in his life. However, Fagin and his associate, the brutal Bill Sikes, fear that Oliver might reveal their secrets and plan to recapture him. They eventually succeed, dragging Oliver back into the criminal underworld.

Throughout the novel, Oliver faces numerous challenges and dangers. He encounters Nancy, Bill Sikes's girlfriend, who becomes sympathetic to Oliver's plight. Nancy secretly helps Oliver and informs Mr. Brownlow of Oliver's whereabouts. However, her actions are discovered by Sikes, leading to her tragic death at his hands.

In the end, Oliver's true heritage is revealed. He is discovered to be the lost nephew of Mr. Brownlow's friend, Mr. Leeford. This discovery secures Oliver's place in a loving and caring home. The novel concludes with Oliver finding peace and happiness, while Fagin is arrested and sentenced to death.

"Oliver Twist" is a powerful critique of the social injustices of Dickens's time, particularly the harsh treatment of orphans and the poor. It explores themes of poverty, crime, and the struggle for justice, making it a timeless classic that continues to resonate with readers.
            """,
            author_id=4,
            publication_year=1838
        ),
        Book(
            title="Der Steppenwolf",
            isbn="9783518031599",
            cover="https://media.suhrkamp.de/mediadelivery/rendition/82e916bd8ab941b7821c921430eed487/-S400/der-steppenwolf_9783518463550_cover.jpg",
            excerpt="""
            "Steppenwolf" is a novel by Hermann Hesse, first published in 1927. The story centers on Harry Haller, a reclusive and introspective man in his late forties who identifies himself as a "Steppenwolf," or wolf of the steppes, symbolizing his feeling of being an outsider in society. Harry sees himself as having a dual nature: one part human and one part wild, untamed wolf. This internal conflict drives the narrative and explores themes of identity, isolation, and the struggle for meaning in life.

The novel begins with Harry renting a room in a quiet boarding house, where he reflects on his life and contemplates suicide. He feels disconnected from the bourgeois society around him and is tormented by his inability to reconcile his spiritual and animalistic sides. One evening, Harry encounters a mysterious man who gives him a pamphlet titled "Treatise on the Steppenwolf." This pamphlet, which seems to be written specifically for him, describes the psychological complexities and dualities of the Steppenwolf, resonating deeply with Harry's own experiences.

As Harry delves deeper into his existential crisis, he meets Hermine, a young woman who becomes his guide and confidante. Hermine introduces Harry to a new world of pleasure and freedom, encouraging him to embrace life and its contradictions. Through Hermine, Harry also meets Pablo, a saxophonist who offers him insights into the world of jazz and sensuality, and Maria, a woman with whom Harry has a passionate affair.

The climax of the novel occurs during a fantastical masquerade ball, where Harry's perceptions of reality and fantasy blur. At the ball, he enters the "Magic Theater," a hallucinatory experience that forces him to confront his deepest fears, desires, and the multiplicity of his own identity. In the Magic Theater, Harry faces surreal and symbolic scenarios that challenge his understanding of self and reality.

Ultimately, "Steppenwolf" is a profound exploration of the human psyche and the quest for self-discovery. Through Harry Haller's journey, Hermann Hesse delves into the themes of individuality, duality, and the search for authenticity in a fragmented world. The novel's complex structure and philosophical depth have made it a classic work of modern literature, resonating with readers who grapple with their own inner conflicts and the search for meaning.
            """,
            author_id=5,
            publication_year=1927
        ),
    ]

    with app.app_context():
        for row in [*authors, *books]:
            db.session.add(row)
        db.session.commit()


with app.app_context() as app_context:
    db.create_all()

if __name__ == "__main__":
    app.run("0.0.0.0", port=3000, debug=True)
