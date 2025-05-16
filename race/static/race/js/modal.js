const modal = document.querySelector("#raceModal");
const modalTitle = document.querySelector("#modal-title");
const modalDate = document.querySelector("#modal-date");
const modalLoc = document.querySelector("#modal-loc");
const modalStatus = document.querySelector("#modal-status");
const modalCourse = document.querySelector("#modal-course");
const modalHome = document.querySelector("#modal-homepage");

document.querySelectorAll(".race-item").forEach(item => {
    item.addEventListener("click", () => {
        const id = item.dataset.id;
        fetch(`/race/detail/${id}/`)
            .then(res => res.json())
            .then(data => {
                modalTitle.innerText = data.title;
                modalDate.innerText = data.date;
                modalLoc.innerText = data.loc;
                modalStatus.innerText = data.status;
                modalCourse.innerText = data.course.join(', ');
                modalHome.innerText = data.homepage;
                modal.style.display = "block";
            });
    });
});

document.querySelector(".close-btn").addEventListener("click", () => {
    modal.style.display = "none";
});

document.querySelector('.modal-overlay').addEventListener('click', () => {
    modal.style.display = 'none';
});
