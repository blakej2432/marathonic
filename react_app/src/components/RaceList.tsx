import { useEffect, useState } from 'react';
import MainFilter, { type FilterType } from './MainFilter';

interface Race {
  id: number;
  title: string;
  date: string;
  region: string;
  city: string;
  course_type: string[];
  race_image: string | null;
}

const initialFilters: FilterType = {
  city: [],
  status: [],
  course: [],
  date_from: [],
  date_to: []
};

function RaceList() {
  const [races, setRaces] = useState<Race[]>([]);
  const [filters, setFilters] = useState<FilterType>(initialFilters);

  useEffect(() => {
    const fetchRaces = async () => {
      try {
        const cleanedParams = Object.entries(filters)
          .filter(([_, v]) => Array.isArray(v) ? v.length > 0 : !!v)
          .flatMap(([key, value]) =>
            Array.isArray(value)
              ? value.map(v => `${encodeURIComponent(key)}=${encodeURIComponent(v)}`)
              : [`${encodeURIComponent(key)}=${encodeURIComponent(value)}`]
          )
          .join('&');

        const response = await fetch(`/race/race_list?${cleanedParams}`);
        if (!response.ok) throw new Error('응답 실패');

        const data: Race[] = await response.json();
        setRaces(data);
      } catch (err) {
        console.error('fetch 요청 실패:', err);
      }
    };

    fetchRaces();
  }, [filters]);

  const toggleFilterValue = (key: keyof FilterType, value: string) => {
    setFilters(prev => {
      const current = prev[key];
      const updated = current.includes(value)
        ? current.filter(v => v !== value)
        : [...current, value];
      return { ...prev, [key]: updated };
    });
  };

  const resetFilters = () => {
    setFilters(initialFilters);
  };

  return (
    <div className="race-list-wrap">
      <MainFilter
        filters={filters}
        toggleFilterValue={toggleFilterValue}
        resetFilters={resetFilters}
      />

      <ul className="race-list">
        {races.map(race => (
          <li key={race.id} className="race-item">
            <div className="race-img">
              <img
                src={race.race_image || '/static/race/images/race-sample.jpg'}
                alt="레이스 이미지"
              />
            </div>
            <div className="race-info">
              <p className="race-title">{race.title}</p>
              <p className="race-date">{race.date}</p>
              <p className="race-loc">{race.region} ({race.city})</p>
              <p className="course">{race.course_type.join(', ')}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RaceList;