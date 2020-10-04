import React, {useState, useEffect} from 'react';
import Navbar from './Navbar';
import Loading from './Loading';
import Article from './Article';


import "../Styles/main.css"

function Main() {
  const [numArticles, setNumArticles] = useState(18);
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // SET TIMEOUT TO 3000 WHEN DONE
    fetch("../data.json")
      .then(res => res.json())
      .then(data => setArticles(data.articles.slice(0,numArticles)))
    setTimeout(() => {
      setLoading(!loading)
      console.log("rerun")
    }, 3000)
  },[])

  return (
    loading
      ?
      <Loading />
      :
      <div className="container">
        <Navbar />
        <div className="article-wrapper">
          {articles.map(currArticle => (
            <Article 
              title={currArticle.Title}
              img={currArticle.LinkToImage}
              articleLink={currArticle.URL}  
            />  
          ))}
        </div>
      </div>
  );
}

export default Main;


// 

// 