import TagItem from "./Tag";

function TagView(props){
    // console.log("this is props in TagView" , props.tagsList)
    return (
        <div>
            <ul>
                {/* {tagVar.map(tags => < TagItems Tags={tags}/>)} */}
                {props.tagsList.map(tags => <TagItem Tags={tags}/>)}
                {/* uncomment the props one, once database is working */}
            </ul>
        </div>
    )
}
export default TagView
