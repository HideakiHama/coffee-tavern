import Tag from "./Tag";

function TagListView(props){
    return (
        <div>
            <ul>
                {props.tagList.map(tag => <Tag Tag={tag}/>)}
            </ul>
        </div>
    )
}
export default TagListView
