    import { CategoryItem } from "../../../CategoryItem/CategoryItem"
    import { useState, useEffect} from "react";
    import axios from "axios";

    import "./category-container.css";

    export const CategoryContainer = () => {
        const [data, setData] = useState([]);

        useEffect(() => {
            axios.get('http://127.0.0.1:8000/api/v1/categorylist/')
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
        }, []);

        return (
            <aside className="category-container-style">
                {data.map(item => (
                    <CategoryItem categoryName={item.name}/>
                ))}
            </aside>
        )
    }