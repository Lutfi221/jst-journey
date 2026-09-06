document.addEventListener('DOMContentLoaded', () => {
    const clapBtn = document.getElementById('clap-btn');
    const flashOverlay = document.getElementById('flash-overlay');
    const takeInput = document.getElementById('take');
    const topStick = document.getElementById('top-stick');

    // Function to generate 0.1 seconds of white noise
    function playWhiteNoise() {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        // Calculate how many audio samples we need for 0.1 seconds
        const frameCount = audioCtx.sampleRate * 0.1;
        
        // Create an empty, 1-channel (mono) audio buffer
        const myArrayBuffer = audioCtx.createBuffer(1, frameCount, audioCtx.sampleRate);
        const channelData = myArrayBuffer.getChannelData(0);

        // Fill the buffer with random numbers between -1.0 and 1.0 (White Noise)
        for (let i = 0; i < frameCount; i++) {
            channelData[i] = Math.random() * 2 - 1;
        }

        // Create an audio source and attach our custom buffer to it
        const noiseSource = audioCtx.createBufferSource();
        noiseSource.buffer = myArrayBuffer;

        // Connect and play
        noiseSource.connect(audioCtx.destination);
        noiseSource.start();
    }

    function flashScreen() {
        flashOverlay.style.opacity = '1';
        setTimeout(() => {
            flashOverlay.style.opacity = '0';
        }, 50); 
    }

    function animateSticks() {
        // Snap the top stick down
        topStick.classList.add('snap-down');

        // Pop it back open after 300 milliseconds
        setTimeout(() => {
            topStick.classList.remove('snap-down');
        }, 300);
    }

    clapBtn.addEventListener('click', () => {
        animateSticks();
        playWhiteNoise();
        flashScreen();

        let currentTake = parseInt(takeInput.value);
        if (!isNaN(currentTake)) {
            takeInput.value = currentTake + 1;
        }
    });
});