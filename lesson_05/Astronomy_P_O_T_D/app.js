const apiKey = "G6ApGN2gysdsGQvTUpGC4dEKlBkjFsrWlkS6aFCj";
const apodUrl = "https://api.nasa.gov/planetary/apod";
fetch(`${apodUrl}?api_key=${apiKey}`)
.then(res=>res.json())
.then(data=>console.log(data));


console.log(dataImage)



// document.querySelector("#date").addEventListener("click",showImage)

// function showImage() {
//     const imageDate = document.querySelector("#date").value
//     console.log(imageDate)
// }

// {
//     "date": "2024-09-16",
//     "explanation": "Why does this large crater on Mercury have two rings and a smooth floor?  No one is sure.  The unusual feature called Vivaldi Crater spans 215 kilometers and was imaged again in great detail by ESA's and JAXA's robotic BepiColombo spacecraft on a flyby earlier this month. A large circular feature on a rocky planet or moon is usually caused by either an impact by a small asteroid or a comet fragment, or a volcanic eruption. In the case of Vivaldi, it is possible that both occurred -- a heavy strike that caused a smooth internal lava flow.  Double-ringed craters are rare, and the cause of the inner rings remains a topic of research.  The speed-slowing gravity-assisted flyby of Mercury by BepiColombo was in preparation for the spacecraft entering orbit around the Solar System's innermost planet in 2026.",
//     "hdurl": "https://apod.nasa.gov/apod/image/2409/MercuryCaloris_BepiColombo_1806.jpg",
//     "media_type": "image",
//     "service_version": "v1",
//     "title": "Mercury's Vivaldi Crater from BepiColombo",
//     "url": "https://apod.nasa.gov/apod/image/2409/MercuryCaloris_BepiColombo_960.jpg"
//   }