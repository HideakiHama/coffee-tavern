import TagItem from "./Tag";

function TagView(props){
    // let tagVar = [{
    //     id: 0,
    //     tag: 'bartender'
    // }, {
    //     id: 1,
    //     tag: 'barista' 
    // }]
    console.log("this is props in TagView" , props.tagsList)
    return (
        <div>
            <ul>
                {/* {tagVar.map(tags => < TagItems Tags={tags}/>)} */}
                {props.tagsList.map( tag => < TagItem Tag={tag}/>)}
                {/* uncomment the props one, once database is working */}
            </ul>
        </div>
    )
}
export default TagView