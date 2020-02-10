import React from 'react'
import CardUI from './cardUI'
const BigCard = () => {
    return (
        <div className="card cd p-3 my-4 big-card border-0">
            <div className="text-left my-auto">
                <h4 className="card-title">HI Bond!!</h4>
                <p className="card-text text-small">"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."</p>
            </div>  
            <div className="card-img my-auto">
                <img src="/images/image5.png"/>
            </div>        
        </div>
    )
}

export default BigCard
