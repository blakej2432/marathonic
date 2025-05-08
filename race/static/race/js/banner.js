const banners = document.querySelectorAll('.banner');
const container = document.querySelector('.banner-slider');

container.classList.add('default');

banners.forEach(banner => {
    banner.addEventListener('mouseenter', () => {
    container.classList.remove('default');
    banners.forEach(b => b.classList.remove('active'));
    banner.classList.add('active');
    });

    banner.addEventListener('mouseleave', () => {
    banners.forEach(b => b.classList.remove('active'));
    container.classList.add('default');
    });
});
