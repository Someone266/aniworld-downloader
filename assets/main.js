const theme = localStorage.getItem('theme');
if (theme) {
    document.documentElement.setAttribute('data-bs-theme', theme);
} else {
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-bs-theme', 'light');
    }
}

// after document loaded
document.addEventListener("DOMContentLoaded", function () {

    const tags = document.getElementById("tags").value;
    const tagsDiv = document.getElementById("tagsDiv");
    tags.split(", ").forEach((tag) => {
        const tagBadge = document.createElement("span");
        tagBadge.className = "badge bg-secondary m-1";
        tagBadge.innerHTML = tag;
        tagsDiv.appendChild(tagBadge);
    });

    // const buttonColors = {
    //     "myanimelist.com": "#2f4e99",
    //     "anidb.net": "#f9a653",
    //     "anilist.co": "#02a9ff",
    //     "anime-planet.com": "#f0574b",
    //     "anisearch.com": "#fedd48",
    //     "kitsu.io": "#e86750",
    //     "livechart.me": "#90a329",
    //     "myanimelist.net": "#2f4e99",
    //     "notify.moe": "#c37d95"
    // };
    // let sources = document.getElementById("sources").value;
    // sources = sources.split(", ");
    // const sourcesDiv = document.getElementById("sourcesDiv");
    // sources.forEach((source) => {
    //     const sourceButton = document.createElement("a");
    //     sourceButton.href = source;
    //     sourceButton.target = "_blank";
    //     sourceButton.className = "btn btn-outline-dark m-1";
    //     sourceButton.style.backgroundColor = buttonColors[source.split("/")[2]];
    //     sourceButton.innerHTML = source.split("/")[2];
    //     sourcesDiv.appendChild(sourceButton);
    // });

    const seasons = document.getElementById("seasons").dataset.seasons;
    const episodes = document.getElementById("episodes").dataset.episodes;
    const seasonsDiv = document.getElementById("seasons");
    const episodesDiv = document.getElementById("episodes");

    // first element of seasonsDiv 
    // <span class="btn btn-primary">Seasons:</span>
    const seasonsLabel = document.createElement("span");
    seasonsLabel.className = "btn btn-primary";
    seasonsLabel.innerHTML = "Seasons:";
    seasonsDiv.innerHTML = "";
    seasonsDiv.appendChild(seasonsLabel);

    // create season and episode buttons based on the number of seasons and episodes
    for (let i = 1; i <= seasons; i++) {
        // example button:
        //                 <button class="btn btn-outline-primary" data-button="season">1</button>
        const seasonButton = document.createElement("button");
        seasonButton.className = "btn btn-outline-primary";
        seasonButton.setAttribute("data-button", "season");
        seasonButton.innerHTML = i;

        seasonsDiv.appendChild(seasonButton);
    }

    // first element of episodesDiv
    // <span class="btn btn-primary">Episodes:</span>
    const episodesLabel = document.createElement("span");
    episodesLabel.className = "btn btn-primary";
    episodesLabel.innerHTML = "Episodes:";
    episodesDiv.innerHTML = "";
    episodesDiv.appendChild(episodesLabel);

    for (let i = 1; i <= episodes; i++) {
        // example button:
        //                                <button class="btn btn-outline-primary" data-button="episode">1</button>
        const episodeButton = document.createElement("button");
        episodeButton.className = "btn btn-outline-primary";
        episodeButton.setAttribute("data-button", "episode");
        episodeButton.innerHTML = i;

        episodesDiv.appendChild(episodeButton);
    }

    document.getElementById('dark-light-mode-toggle').setAttribute('data-event-listener', 'true');
    // add transition when theme changes
    document.getElementById('dark-light-mode-toggle').addEventListener('click', function () {
        var theme = document.documentElement.getAttribute('data-bs-theme');
        if (theme == 'dark') {
            theme = 'light';
        } else {
            theme = 'dark';
        }
        console.log('theme: ' + theme);
        document.documentElement.setAttribute('data-bs-theme', theme);

        localStorage.setItem('theme', theme);
    });

    // add event listener to all season buttons
    document.querySelectorAll('[data-button="season"]').forEach((button) => {
        button.addEventListener("click", function () {
            // remove active class from all buttons
            document.querySelectorAll('[data-button="season"]').forEach((button) => {
                button.classList.remove("active");
            });
            // add active class to the clicked button
            this.classList.add("active");
            watchVideo();
        });
    });
    // add event listener to all episode buttons
    document.querySelectorAll('[data-button="episode"]').forEach((button) => {
        button.addEventListener("click", function () {
            // remove active class from all buttons
            document.querySelectorAll('[data-button="episode"]').forEach((button) => {
                button.classList.remove("active");
            });
            // add active class to the clicked button
            this.classList.add("active");
            watchVideo();
        });
    });
});

function watchVideo() {
    // get active season and episode
    const season = document.querySelector('[data-button="season"].active').innerHTML;
    const episode = document.querySelector('[data-button="episode"].active').innerHTML;

    // if no season or episode is selected, return
    if (!season || !episode) {
        return;
    }

    // generate video link
    let videoLink = './video/' + season + '/' + episode + '.mp4';
    // check if video exists, by only fetching the headers
    fetch(videoLink, {
        method: 'HEAD'
    }).then(response => {
        if (response.ok) {
            // set src attribute of the video element
            document.getElementById('player-container').classList.remove('d-none');
            document.getElementById('player').src = videoLink;
            // remove d-none class from the video element, if set
            document.getElementById('select-episode-first').classList.add('d-none');
            document.getElementById('video-not-found').classList.add('d-none');
            document.getElementById('direct-link').classList.remove('d-none');
            document.getElementById('direct-link').href = videoLink;
            return;
        } else {
            // set d-none class to the video element, if not already set
            document.getElementById('player-container').classList.add('d-none');
            document.getElementById('player').src = '';
            document.getElementById('select-episode-first').classList.add('d-none');
            document.getElementById('direct-link').classList.add('d-none');
            document.getElementById('video-not-found').classList.remove('d-none');
            return;
        }
    }).catch(() => {
        // set d-none class to the video element, if not already set
        document.getElementById('player-container').classList.add('d-none');
        document.getElementById('player').src = '';
        document.getElementById('select-episode-first').classList.add('d-none');
        document.getElementById('direct-link').classList.add('d-none');
        document.getElementById('video-not-found').classList.remove('d-none');
        return;
    });       
}
