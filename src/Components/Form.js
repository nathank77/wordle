import "../Styles/Form.css"

import React, { useEffect, useState } from 'react';
import { Formik} from 'formik';

function Form() {

  const [movie, setMovie] = useState(null);  
  const [guess, setGuess] = useState(0);

  const [prevGuesses, setPrevGuesses] = useState([]);

  async function fetchMovie (enteredMovie) {
    fetch(`/api/search-movie/${enteredMovie}`).then(res => res.json()).then(data => {
      setMovie({ 
        Title: data.Title, 
        Director: data.Director,
        ReleaseDate: data.ReleaseDate,
        BoxOfficeGross: data.BoxOfficeGross,
        Runtime: data.Runtime,
        imdbRating: data.imdbRating,
        id: guess
      });
    });
  }

  function incrementGuesses() {
    setGuess(guess + 1);
  }

  function addPrevGuess(pg) {
    const temp = prevGuesses.slice();
    temp.push(pg);
    setPrevGuesses(temp);
  }

  return (
    <div>
      <h1>Hi, enter a movie :)!</h1>
      <h2>current guesses: {guess}</h2>

       {guess > 1 ? (
        <div>
        <h6>Old guesses </h6>
        <ul className='no-bullets'>
          {prevGuesses.map((pg) =>
          <li key={pg.id}> 
            <p> Title: {pg.Title},  
            Director: {pg.Director}, 
            Release Date: {pg.ReleaseDate}, 
            US Box Office: {pg.BoxOfficeGross},
            Running Time: {pg.Runtime},
            IMDB Rating: {pg.imdbRating}</p>
          </li>)}
        </ul>
        </div>
      ) : null}

      {movie ? (<div>
        <h4>Current Movie Title is: {movie.Title}</h4>
        <p>Director: {movie.Director}</p>
        <p>Release Date: {movie.ReleaseDate}</p>
        <p>US Box Office: {movie.BoxOfficeGross}</p>
        <p>Running Time: {movie.Runtime}</p>
        <p>IMDB Rating: {movie.imdbRating}</p>
      </div>) : null }


      <Formik
        initialValues={{
          movie: ""
        }}
        onSubmit={async (values, { setSubmitting }) => {

          if (guess != 0) addPrevGuess(movie);
          fetchMovie(values.movie);
          incrementGuesses();
          setSubmitting(false);
        }}
      >
        {({
          values, 
          errors, 
          touched, 
          handleChange,
          handleBlur,
          handleSubmit,
          isSubmitting
        }) => (
          <form onSubmit={handleSubmit}>
            <input 
              type="text"
              name="movie"
              onChange={handleChange}
              onBlur={handleBlur}
              value={values.movie}
            />
            <button type="submit" disabled={isSubmitting}>
               Submit
            </button>
          </form>
        )}
      </Formik>
    </div>
  )
}

export default Form;