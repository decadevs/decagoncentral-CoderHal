import React from 'react'
import CardUI from './cardUI'

const Cards = () => {
    return (
        <div className="">
            
            <div className="row">
                <div className="col-md-6">
                    <CardUI
                    src="/images/image2.png"
                    title="Find an employee"
                    text="Change your profile name, picture, twitter handle and bio."
                    link="Search Employee"
                    />
                </div>

                <div className="col-md-6">
                    <CardUI
                    src="/images/image3.png"
                    title="Find a Dev"
                    text="Change your profile name, picture, twitter handle and bio."
                    link="Search Dev"
                    />
                </div>

                <div className="col-md-6">
                    <CardUI
                    src="/images/image1.png"
                    title="Update profile"
                    text="Change your profile name, picture, twitter handle and bio."
                    link="Update profile"
                    />
                </div>

                <div className="col-md-6">
                    <CardUI
                    src="/images/image4.png"
                    title="Update Password"
                    text="Update your password."
                    link="Update profile"
                    />
                </div>
            </div>
        </div>
    );
}

export default Cards;


