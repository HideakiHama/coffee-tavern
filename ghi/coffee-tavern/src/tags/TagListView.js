import axios from "axios";
import TagItems from "./Tags";

function TagView(props){
    // let tagVar = [{
    //     id: 0,
    //     tag: 'bartender'
    // }, {
    //     id: 1,
    //     tag: 'barista' 
    // }]
    return (
        <div>
            <ul>
                {/* {tagVar.map(tags => < TagItems Tags={tags}/>)} */}
                {props.tagsList.map(tags => < TagItems Tags={tags}/>)}
                {/* uncomment the props one, once database is working */}
            </ul>
        </div>
    )
}
export default TagView