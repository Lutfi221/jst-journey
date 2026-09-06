// 1. Setup the Scene
const scene = new THREE.Scene();

// 2. Setup the Camera (Field of View, Aspect Ratio, Near plane, Far plane)
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5; // Move the camera back so we can view the object

// 3. Setup the Renderer
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement); // Inject the canvas into the HTML

// 4. Create a 3D Object (Geometry + Material = Mesh)
const geometry = new THREE.BoxGeometry(2, 2, 2); // Width, height, depth
const material = new THREE.MeshBasicMaterial({ color: 0x00ff88, wireframe: true }); // Green wireframe
const cube = new THREE.Mesh(geometry, material);
scene.add(cube); // Add the cube to our world

// 5. Animation Loop (Renders the scene roughly 60 times per second)
function animate() {
    requestAnimationFrame(animate);

    // Rotate the cube on the X and Y axes
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    // Render the updated scene from the camera's perspective
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.render(scene, camera);
}

// Start the animation
animate();

