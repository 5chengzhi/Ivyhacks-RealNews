import React from 'react'
import "../Styles/article.css";


export default function Article({title, img, articleLink}) {
    return (
        <div className="main-article">
            <div className="img-wrapper" style={{backgroundImage: `url(${img})`}}></div>
            <h1 className="article-title"><a href={articleLink} target="_blank">{title.substring(0,35)}...</a></h1>  
        </div>
    )
}
