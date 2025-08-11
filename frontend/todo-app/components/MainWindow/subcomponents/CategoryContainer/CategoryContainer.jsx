import { CategoryItem } from "../../../CategoryItem/CategoryItem"

import "./category-container.css"

export const CategoryContainer = () => {
    return (
        <aside className="category-container-style">
            <CategoryItem />
            <CategoryItem />
            <CategoryItem />
            <CategoryItem />
        </aside>
    )
}