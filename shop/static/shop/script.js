// Show confirmation when adding to cart
function addToCartAlert() {
    alert('Product added to cart!');
}

// Attach event listeners to Add to Cart buttons
window.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a.button[href^="/add-to-cart/"]').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            addToCartAlert();
        });
    });
    // Smooth scroll to top on navigation
    document.querySelectorAll('nav a').forEach(function(link) {
        link.addEventListener('click', function(e) {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });
});

document.querySelectorAll('.product-card').forEach(card => {
  // Click event to activate the card
  card.addEventListener('click', function() {
    // Remove active class from all cards
    document.querySelectorAll('.product-card').forEach(c => c.classList.remove('active'));
    // Add active class to clicked card
    this.classList.add('active');
    // Get dominant color from product image (placeholder)
    const img = this.querySelector('img');
    if (img) {
      const dominantColor = getDominantColor(img); // Placeholder function
      this.style.setProperty('--product-bg-color', dominantColor);
      this.dataset.bgColor = dominantColor;
    }
  });
  // Mouse move effect for floating particles
  card.addEventListener('mousemove', function(e) {
    const rect = this.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    this.style.setProperty('--x', `${x}px`);
    this.style.setProperty('--y', `${y}px`);
  });
});

// Example function to get dominant color (placeholder)
function getDominantColor(imgElement) {
  // This is a placeholder - implement actual color extraction for real effect
  return 'linear-gradient(135deg, #6366f1 0%, #14b8a6 100%)';
}

document.addEventListener('mousemove', function(e) {
  const x = e.clientX / window.innerWidth * 100;
  const y = e.clientY / window.innerHeight * 100;
  document.body.style.setProperty('--mouse-x', `${x}%`);
  document.body.style.setProperty('--mouse-y', `${y}%`);
  document.body.classList.add('mouse-effect');
});

document.querySelectorAll('.register-btn').forEach(btn => {
  // Create particles on hover
  btn.addEventListener('mouseenter', function() {
    for (let i = 0; i < 12; i++) {
      const particle = document.createElement('span');
      particle.classList.add('particles');
      particle.style.left = `${Math.random() * 100}%`;
      particle.style.top = `${Math.random() * 100}%`;
      particle.style.animationDelay = `${Math.random() * 0.5}s`;
      particle.style.width = `${2 + Math.random() * 4}px`;
      particle.style.height = particle.style.width;
      this.appendChild(particle);
      // Remove particle after animation
      setTimeout(() => {
        particle.remove();
      }, 1500);
    }
  });
  // Mouse move effect for dynamic lighting
  btn.addEventListener('mousemove', function(e) {
    const rect = this.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    this.style.setProperty('--mouse-x', `${x}px`);
    this.style.setProperty('--mouse-y', `${y}px`);
  });
}); 