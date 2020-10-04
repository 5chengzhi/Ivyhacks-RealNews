import React, {useState, useEffect} from 'react';
import Navbar from './Navbar';
import Loading from './Loading';

import "../Styles/main.css"

function Main() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setArticles([1,2,3,4,5])
      setLoading(!loading)
    }, 3000)
  },[])
  return (
    loading
      ?
      <Loading />
      :
      <div className="container">
        <Navbar />
        <h6>{articles[0]}</h6>
        <h6>{articles[1]}</h6>
      </div>
  );
}

export default Main;
