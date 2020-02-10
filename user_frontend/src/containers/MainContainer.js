import React from 'react'
import Cards from '../components/Cards'
import BigCard from '../components/BigCard'
import Header from '../components/Header'

const MainContainer = () => {
    return (
      <div className="col-sm-9">
        <div className="w-75 m-auto pt-5">
            <Header/>
            <BigCard/>
            <Cards/>
        </div>
      </div>
    )
}

export default MainContainer
