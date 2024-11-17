from data_models import db, Author, Book
from random import randrange

def data_population(app):
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
            rating=randrange(20, 50)/10,
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
            rating=randrange(20, 50)/10,
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
            rating=randrange(20, 50)/10,
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
            rating=randrange(20, 50)/10,
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
            rating=randrange(20, 50)/10,
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
        Book(
            title="Die Pickwickier",
            rating=randrange(20, 50)/10,
            isbn="9780758336606",
            cover="https://images.thalia.media/00/-/ef803e2b6db0473eac5dd7840a2c0068/die-pickwickier-epub-charles-dickens.jpeg",
            excerpt="""
                "The Pickwick Papers," originally titled "The Posthumous Papers of the Pickwick Club," is the first novel by Charles Dickens, published in serialized form from 1836 to 1837. The story revolves around Samuel Pickwick, Esquire, and his fellow members of the Pickwick Club as they travel around England to observe and report on the various facets of English life. This comic masterpiece is filled with humor, satire, and a cast of eccentric characters.

    The novel begins with the formation of the Pickwick Club by Samuel Pickwick, a kind-hearted and wealthy gentleman. He appoints three other members to accompany him on their adventures: Tracy Tupman, a romantic and somewhat overweight man; Augustus Snodgrass, an aspiring but untalented poet; and Nathaniel Winkle, an inept sportsman. The group sets off on a series of journeys, aiming to gather experiences and observations to share with the Club.

    One of their first adventures takes them to Rochester, where they encounter the conniving Alfred Jingle, who deceives and manipulates the Pickwickians for his gain. Despite Jingle's trickery, the Pickwick Club continues their travels, often finding themselves in humorous and often absurd situations. For instance, Tupman falls in love with Rachael Wardle, a middle-aged woman, leading to a series of comedic misunderstandings.

    Throughout the novel, the Pickwickians encounter a variety of colorful characters, including the bumbling lawyer Mr. Perker, the pompous medical student Bob Sawyer, and the ever-loyal servant Sam Weller, who becomes Mr. Pickwick's personal valet. Sam Weller quickly becomes one of the most beloved characters, known for his witty remarks and street-smart wisdom.

    The novel's central plot involves Mr. Pickwick's legal troubles. After being tricked by his landlady, Mrs. Bardell, who sues him for breach of promise of marriage, Mr. Pickwick finds himself entangled in a farcical courtroom drama. Despite his innocence, he is sentenced to a debtors' prison because he refuses to pay the damages on principle. His time in the Fleet Prison exposes him to the harsh realities of the English legal system and the plight of the poor.

    Sam Weller's loyalty and ingenuity play a crucial role in Mr. Pickwick's eventual release from prison. The novel concludes with the dissolution of the Pickwick Club, as the members go their separate ways. Mr. Pickwick retires to a peaceful life in the countryside, surrounded by friends and content with the knowledge that he has enriched the lives of those around him.

    "The Pickwick Papers" is celebrated for its rich characterization, humor, and social commentary. Dickens's keen observations and ability to create memorable characters laid the foundation for his future works and cemented his reputation as one of the greatest novelists of the 19th century.
                """,
            author_id=4,
            publication_year=1837
        ),
        Book(
            title="The Trial",
            rating=randrange(20, 50)/10,
            isbn="978-0-14-118290-8",
            cover="http://bookcoverarchive.com/wp-content/uploads/amazon/the_trial.jpg",
            excerpt="""
             "The Trial" by Franz Kafka is a haunting narrative of Josef K., a man who finds himself arrested by a mysterious authority for an unspecified crime. The story delves into themes of bureaucracy, guilt, and the surreal nature of existence. As Josef navigates the absurd and labyrinthine judicial system, he faces a series of bizarre and frustrating obstacles. Kafka's work explores the dehumanizing effects of an impersonal legal system and raises questions about the nature of justice and the individual's role within society. The novel's unsettling atmosphere and existential undertones leave a lasting impact on readers, making it a seminal work in modern literature.
             """,
            author_id=1,
            publication_year=1925
        ),
        Book(
            title="Great Expectations",
            rating=randrange(20, 50)/10,
            isbn="978-0-14-143956-0",
            cover="https://m.media-amazon.com/images/I/51evTcoKMGL._SY445_SX342_.jpg",
            excerpt=""" "Great Expectations" by Charles Dickens follows the life of Pip, an orphan who dreams of becoming a gentleman. Through a series of unexpected events, he inherits a fortune from a mysterious benefactor and moves to London to fulfill his aspirations. The novel explores themes of social class, ambition, and personal growth. Dickens's vivid characters and intricate plot capture the struggles and triumphs of Victorian society. Pip's journey of self-discovery and his encounters with figures such as the enigmatic Miss Havisham and the kind-hearted Joe Gargery offer a poignant reflection on human values and the true meaning of wealth and success. """,
            author_id=4,
            publication_year=1861
        ),
        Book(
            title="The Metamorphosis",
            rating=randrange(20, 50)/10,
            isbn="978-0-14-243718-2",
            cover="https://m.media-amazon.com/images/I/51c9pTFcU6L._SY445_SX342_.jpg",
            excerpt=""" "The Metamorphosis" by Franz Kafka tells the story of Gregor Samsa, a traveling salesman who wakes up one morning to find himself transformed into a giant insect. The novella explores themes of alienation, identity, and the absurdity of human existence. As Gregor struggles to adapt to his new condition, he becomes increasingly isolated from his family and society. Kafka's narrative delves into the psychological and existential implications of Gregor's transformation, highlighting the fragility of human connections and the dehumanizing effects of modern life. The story's dark and surreal tone has made it a cornerstone of 20th-century literature. """,
            author_id=1,
            publication_year=1915
        ),
        Book(
            title="The Importance of Being Earnest",
            rating=randrange(20, 50)/10,
            isbn="978-0-19-953597-7",
            cover="https://medien.umbreitkatalog.de/bildzentrale/978/147/354/5632.jpg",
            excerpt=""" "The Importance of Being Earnest" by Oscar Wilde is a comedic play that satirizes the social conventions and trivialities of the Victorian era. The plot revolves around two young men, Jack Worthing and Algernon Moncrieff, who create alter egos named "Ernest" to escape their social obligations and win the hearts of the women they love. Wilde's witty dialogue and humorous situations expose the absurdities and hypocrisies of high society. The play's enduring charm lies in its clever wordplay and timeless critique of social pretensions, making it one of Wilde's most beloved works. """,
            author_id=2,
            publication_year=1895
        ),
        Book(
            title="The Shining",
            rating=randrange(20, 50)/10,
            isbn="978-0-385-12167-5",
            cover="https://m.media-amazon.com/images/I/51ImsilVpvL._SY445_SX342_.jpg",
            excerpt=""" "The Shining" by Stephen King is a psychological horror novel that follows Jack Torrance, an aspiring writer and recovering alcoholic who takes a job as the winter caretaker of the isolated Overlook Hotel. Jack brings his wife Wendy and young son Danny, who possesses psychic abilities known as "the shining." As the winter progresses, the hotel's malevolent influence exacerbates Jack's descent into madness, putting his family in grave danger. King's masterful storytelling and exploration of themes such as isolation, addiction, and the supernatural make "The Shining" a gripping and terrifying read. """,
            author_id=3,
            publication_year=1977
        ),
        Book(
            title="A Tale of Two Cities",
            rating=randrange(20, 50)/10,
            isbn="978-0-14-143960-7",
            cover="https://m.media-amazon.com/images/I/51cLin22oLL._SY445_SX342_.jpg",
            excerpt=""" "A Tale of Two Cities" by Charles Dickens is a historical novel set during the tumultuous years of the French Revolution. The story centers on the lives of Charles Darnay, a French aristocrat, and Sydney Carton, a dissolute English lawyer, whose fates become intertwined. Through themes of sacrifice, resurrection, and the struggle for justice, Dickens weaves a narrative that contrasts the brutality of the Reign of Terror with the personal redemption of his characters. The novel's iconic opening line, "It was the best of times, it was the worst of times," encapsulates the dualities of the era and the enduring human spirit. """,
            author_id=4,
            publication_year=1859
        ),
        Book(
            title="Siddhartha",
            rating=randrange(20, 50)/10,
            isbn="978-0-14-243718-6",
            cover="https://m.media-amazon.com/images/I/515Qwan3blL._SY445_SX342_.jpg",
            excerpt=""" "Siddhartha" by Hermann Hesse is a philosophical novel that follows the spiritual journey of a young man named Siddhartha during the time of the Buddha. Dissatisfied with the teachings of his father and the ascetics, Siddhartha embarks on a quest for enlightenment that leads him through various phases of life, including wealth, sensuality, and asceticism. Ultimately, he finds peace and understanding through his connection with the river and the realization of the unity of all existence. Hesse's novel is a profound exploration of self-discovery, inner peace, and the nature of true wisdom. """,
            author_id=5,
            publication_year=1922
        )
    ]

    with app.app_context():
        for row in [*authors, *books]:
            db.session.add(row)
            db.session.commit()
