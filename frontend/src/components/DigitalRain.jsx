import { useEffect, useRef } from 'react'

const DigitalRain = () => {
    const canvasRef = useRef(null)

    useEffect(() => {
        const canvas = canvasRef.current
        const ctx = canvas.getContext('2d')

        let width = canvas.width = window.innerWidth
        let height = canvas.height = window.innerHeight

        const columns = Math.floor(width / 20)
        const drops = []

        for (let i = 0; i < columns; i++) {
            drops[i] = 1
        }

        const characters = '01' // Binary rain for cyber feel

        const draw = () => {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)' // Fade effect
            ctx.fillRect(0, 0, width, height)

            ctx.fillStyle = '#00f2fe' // Neon Cyan
            ctx.font = '15px monospace'

            for (let i = 0; i < drops.length; i++) {
                const text = characters.charAt(Math.floor(Math.random() * characters.length))
                ctx.fillText(text, i * 20, drops[i] * 20)

                if (drops[i] * 20 > height && Math.random() > 0.975) {
                    drops[i] = 0
                }

                drops[i]++
            }
        }

        const interval = setInterval(draw, 33)

        const handleResize = () => {
            width = canvas.width = window.innerWidth
            height = canvas.height = window.innerHeight
        }

        window.addEventListener('resize', handleResize)

        return () => {
            clearInterval(interval)
            window.removeEventListener('resize', handleResize)
        }
    }, [])

    return (
        <canvas
            ref={canvasRef}
            style={{
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                height: '100%',
                zIndex: 0,
                opacity: 0.3
            }}
        />
    )
}

export default DigitalRain
