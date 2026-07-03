const start = document.querySelectorAll(".start");
const quizz = document.getElementById("quizz-container");
const decision = document.getElementById("decision");
let score = 0;
const scorespan = document.getElementById("score"); 
const scorecontainer= document.getElementById("score-container");


//Definition of quizzes bojects with structure id, question , choices and answer
const qwizzs=  [
    {
        id: 1,
        question:   "What is the capital of Cameroun?",
        choices:    ["Douala", "Garoua", "yaounde", "Bafoussam"],
        solution:   2
    },
    {
        id: 2,
        question:   "Who is the prime minister?",
        choices:    ["Samuel Eto'o", "Joseph Dion Ngute", "Philemon Yann", "Paul Biya"],
        solution:   1
    },
    {
        id: 3,
        question:   "How Many regions count Cameroon?",
        choices:    ["10", "14", "8", "11"],
        solution:   0
    },
    {
        id: 4,
        question:   "In which division is located Dschang?",
        choices:    ["Mifi", "Menoua", "Bamboutos", "None of them"],
        solution:   1
    },
    {
        id: 5,
        question:   "The name of the Senegalese national team is :",
        choices:    ["The Lions", "Atlas'Lions", "Senegal'Lions", "None of them"],
        solution:   3
    },
    {
        id: 6,
        question:   "Which country(ies) organizes the World Cup 2026 ?",
        choices:    ["Mexico", "USA", "Canada", "All of them"],
        solution:   3
    },
    {
        id: 7,
        question:   "How many champion'sLeague has Real Madrid ?",
        choices:    ["10", "14", "15", "16"],
        solution:   2
    },
    {
        id: 8,
        question:   "Who is the best scorer of World Cup history ?",
        choices:    ["Kylian Mbappe", "Lionnel Messi", "Cristiono Ronaldo", "Jonnathan Klose"],
        solution:   1
    },
    {
        id: 9,
        question:   "Who is Michael Jackson ",
        choices:    ["Actor", "Athlete", "Nicola Jackson brother", "Singer"],
        solution:   3
    },
    {
        id: 10,
        question:   "Which country don't share frontieres with China ?",
        choices:    ["Russia", "India", "Japan", "Thailand"],
        solution:   2
    }
];
//Actual question
let currentIndex = 0;


start.forEach(button =>{
button.addEventListener("click", function(event) {
    event.preventDefault();
    score= 0;
    //Display of the first question by default
    currentIndex=0;
    scorecontainer.style.display="none";
    decision.style.display="none";
    document.getElementById("welcome-container").style.display = "none";
    display(currentIndex);
    
    quizz.style.display = "block";
    // console.log(qwizzs[0]);
   
    
});})

//displaying a question with its choices and a button to go to the next question
function display(q) {
    quizz.innerHTML = `   
        <div class="question" style="">
            <p>Question ${q+1}:${qwizzs[q].question}</p>
            <ul>
                <li>
                    <label class="choice">
                        <input type="radio" name="q${q+1}" value="0"> A. ${qwizzs[q].choices[0]}
                    </label>
                </li>
                <li>
                    <label class="choice">
                        <input type="radio" name="q${q+1}" value="1"> B. ${qwizzs[q].choices[1]}
                    </label>
                </li>
                <li>
                    <label class="choice">
                        <input type="radio" name="q${q+1}" value="2"> C. ${qwizzs[q].choices[2]}
                    </label>
                </li>
                <li>
                    <label class="choice">
                        <input type="radio" name="q${q+1}" value="3"> D. ${qwizzs[q].choices[3]}
                    </label>
                </li>
            </ul>
            <button id="btn-next" class="btn">Next</button>
        </div>`;
    btnNext = document.getElementById("btn-next");
    btnNext.addEventListener("click", function(e){
        e.preventDefault();
        checkResult(currentIndex);
        currentIndex +=1 ;
        if (currentIndex>9) {
            scorespan.innerHTML = `<span id="score">${score}</span>`
            scorecontainer.style.display="block";
            btnNext.style.display='none';

        } else {
            console.log(currentIndex, q);
            display(currentIndex);
        }
    });
}

//verification of the answer and display of the result
function checkResult(q){
    const choice = document.querySelector(`input[name="q${q+1}"]:checked`).value;
    console.log(choice);
    if (parseInt(choice)  == qwizzs[q].solution) {
        decision.innerHTML = `<div class="success" > Excellent you get it !!!!</div>`;
        score++;
        console.log("BOnne reponse votre nouveau score est "+ score);
    }
    else{
        decision.innerHTML = `<div class="fail" > False The real answer is ${qwizzs[q].choices[qwizzs[q].solution]}</div>`;
        // console.log(choice);
        // console.log(qwizzs[q].solution);
        console.log("False the good answer is : "+ qwizzs[q].choices[qwizzs[q].solution]);
    }
}