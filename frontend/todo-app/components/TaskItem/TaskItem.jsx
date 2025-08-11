import "./task-item.css"

export const TaskItem = () => {
    return (
        <div className="task-item-style">
            <div className="task-item-header">
                <div className="task-item-header-title">
                    <h2>Task Item Header</h2>
                </div>
                <div className="task-item-header-menu">
                    ...
                </div>
            </div>
            <div className="task-item-description">
                Simple task description
            </div>
            <div className="task-item-footer">
                <div className="task-item-footer-tags">
                    <div>Tag1</div>
                    <div>Tag2</div>
                    <div>Tag3</div>
                </div>
                <div className="task-item-footer-status">
                    <div className="task-item-footer-checkbox">
                        <div></div>
                    </div>
                    <div className="task-item-footer-name">
                        Done
                    </div>
                </div>
            </div>
        </div>
    )
}