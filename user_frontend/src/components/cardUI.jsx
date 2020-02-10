import React from 'react'
const CardUI = (props) => {
    return (
        <div className="card cd p-3 my-4">
            <div className="text-left my-auto">
                <h4 className="card-title">{props.title}</h4>
                <p className="card-text text-small">{props.text}</p>
                <a href="#">{props.link}</a>
            </div>  
            <div className="card-img my-auto">
                <img src={props.src}/>
            </div>        
        </div>
    )
}

export default CardUI
