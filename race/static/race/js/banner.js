const banners = document.querySelectorAll('.banner');

banners.forEach(banner => {
    banner.addEventListener('mouseenter', () => {
    banners.forEach(b => b.classList.remove('active'));
    banner.classList.add('active');
    });

    banner.addEventListener('mouseleave', () => {
    banner.classList.remove('active');
    banners[0].classList.add('active');
    });
});
