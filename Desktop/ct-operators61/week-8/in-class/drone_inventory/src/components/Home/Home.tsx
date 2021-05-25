import React from 'react';

interface Props{
    title: string
}

export const Home = ( props:Props ) => {
    return (
        <div>
            <h1>Title: {props.title}</h1>
            <h1>Hello World fom Operators 61!</h1>
        </div>
    )
}