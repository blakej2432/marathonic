import ReactDOM from 'react-dom/client';
import RaceList from '../components/RaceList';

const raceListWrap = document.querySelector('#race-list-wrap');

if (raceListWrap) {
  const root = ReactDOM.createRoot(raceListWrap);
  root.render(<RaceList />);
}