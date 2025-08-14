import "./category-item.css"

export const CategoryItem = ({categoryName}) => {
    return (
        <div className="category-item-style">
            <div className="category-item-tag-color">
            </div>
            <div className="category-item-tag-name">
                {categoryName}
            </div>
        </div>
    )
}