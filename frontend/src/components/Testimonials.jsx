import React from 'react'

const testimonials = [
    {
        id: 1,
        name: "Sarah Connor",
        role: "CISO, CyberDyne Systems",
        quote: "Vanguard AI caught a sophisticated spear-phishing attack that bypassed our legacy filters. It's an essential layer of defense.",
        rating: 5
    },
    {
        id: 2,
        name: "David Lightman",
        role: "Lead Security Analyst, WOPR Inc.",
        quote: "The speed and accuracy of the logistic regression model are impressive. It gives our team the confidence to act fast.",
        rating: 5
    },
    {
        id: 3,
        name: "Elliot Alderson",
        role: "Cybersecurity Consultant, Allsafe",
        quote: "Finally, a tool that understands the nuance of social engineering. The real-time threat feed is a game changer.",
        rating: 5
    }
]

const Testimonials = () => {
    return (
        <div className="testimonials-section">
            <h2 className="section-title">TRUSTED BY INDUSTRY LEADERS</h2>
            <div className="testimonials-grid">
                {testimonials.map((testimonial) => (
                    <div key={testimonial.id} className="glass-card testimonial-card">
                        <div className="quote-icon">❝</div>
                        <p className="testimonial-quote">"{testimonial.quote}"</p>
                        <div className="testimonial-author">
                            <div className="author-info">
                                <h4>{testimonial.name}</h4>
                                <span>{testimonial.role}</span>
                            </div>
                            <div className="rating">
                                {[...Array(testimonial.rating)].map((_, i) => (
                                    <span key={i}>★</span>
                                ))}
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Testimonials
