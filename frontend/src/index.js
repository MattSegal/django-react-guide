import React from 'react'
import ReactDOM from 'react-dom'

// Define the React app
const App = () => {
    const [count, setCount] = React.useState(0)
    const onClick = () => setCount(c => c + 1)
    return (
        <div>
            <h1>The count is {count}</h1>
            <button onClick={onClick}>Count</button>
        </div>
    )
}
// Mount the app to the mount point.
const root = document.getElementById('app')
ReactDOM.render(<App />, root)
