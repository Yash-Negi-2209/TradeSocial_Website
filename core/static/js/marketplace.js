/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close');

/* Menu show */
if(navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu');
    });
}

/* Menu hidden */
if(navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu');
    });
}

// ========= Filter by Category =================================

document.addEventListener("DOMContentLoaded", function() {
    const categoryTitle = document.querySelectorAll('.category-title');
    const allCategoryPosts = document.querySelectorAll('.all');
    const postsContainer = document.querySelector('.posts-main-container'); 

    categoryTitle.forEach(title => {
        title.addEventListener('click', () => filterPosts(title));
    });

    function filterPosts(item) {
        changeActivePosition(item);
        allCategoryPosts.forEach(post => {
            if (post.classList.contains(item.id)) {
                post.style.display = "block";
                postsContainer.appendChild(post);
            } else {
                post.style.display = "none";
            }
        });
    }

    function changeActivePosition(activeItem) {
        categoryTitle.forEach(title => {
            title.classList.remove('active');
        });
        activeItem.classList.add('active');
    }
});


/*=============== OWL CAROUSEL ===============*/
$(document).ready(function(){
    $(".slider").owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000, // 2000ms = 2s
        autoplayHoverPause: true,
    });
});
