from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

class SearchHit(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new searchHit and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The _id property
        self.__id: Optional[str] = None
        # The _score property
        self.__score: Optional[int] = None
        # The _source property
        self.__source: Optional[entity.Entity] = None
        # The _summary property
        self.__summary: Optional[str] = None
        # The name of the content source that the externalItem is part of.
        self._content_source: Optional[str] = None
        # The internal identifier for the item. The format of the identifier varies based on the entity type. For details, see hitId format.
        self._hit_id: Optional[str] = None
        # Indicates whether the current result is collapses when the collapseProperties property is used.
        self._is_collapsed: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The rank or the order of the result.
        self._rank: Optional[int] = None
        # The resource property
        self._resource: Optional[entity.Entity] = None
        # ID of the result template for rendering the search result. This ID must map to a display layout in the resultTemplates dictionary, included in the searchresponse as well.
        self._result_template_id: Optional[str] = None
        # A summary of the result, if a summary is available.
        self._summary: Optional[str] = None
    
    @property
    def _id(self,) -> Optional[str]:
        """
        Gets the _id property value. The _id property
        Returns: Optional[str]
        """
        return self.__id
    
    @_id.setter
    def _id(self,value: Optional[str] = None) -> None:
        """
        Sets the _id property value. The _id property
        Args:
            value: Value to set for the _id property.
        """
        self.__id = value
    
    @property
    def _score(self,) -> Optional[int]:
        """
        Gets the _score property value. The _score property
        Returns: Optional[int]
        """
        return self.__score
    
    @_score.setter
    def _score(self,value: Optional[int] = None) -> None:
        """
        Sets the _score property value. The _score property
        Args:
            value: Value to set for the _score property.
        """
        self.__score = value
    
    @property
    def _source(self,) -> Optional[entity.Entity]:
        """
        Gets the _source property value. The _source property
        Returns: Optional[entity.Entity]
        """
        return self.__source
    
    @_source.setter
    def _source(self,value: Optional[entity.Entity] = None) -> None:
        """
        Sets the _source property value. The _source property
        Args:
            value: Value to set for the _source property.
        """
        self.__source = value
    
    @property
    def _summary(self,) -> Optional[str]:
        """
        Gets the _summary property value. The _summary property
        Returns: Optional[str]
        """
        return self.__summary
    
    @_summary.setter
    def _summary(self,value: Optional[str] = None) -> None:
        """
        Sets the _summary property value. The _summary property
        Args:
            value: Value to set for the _summary property.
        """
        self.__summary = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def content_source(self,) -> Optional[str]:
        """
        Gets the contentSource property value. The name of the content source that the externalItem is part of.
        Returns: Optional[str]
        """
        return self._content_source
    
    @content_source.setter
    def content_source(self,value: Optional[str] = None) -> None:
        """
        Sets the contentSource property value. The name of the content source that the externalItem is part of.
        Args:
            value: Value to set for the content_source property.
        """
        self._content_source = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchHit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchHit
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchHit()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "contentSource": lambda n : setattr(self, 'content_source', n.get_str_value()),
            "hitId": lambda n : setattr(self, 'hit_id', n.get_str_value()),
            "isCollapsed": lambda n : setattr(self, 'is_collapsed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(entity.Entity)),
            "resultTemplateId": lambda n : setattr(self, 'result_template_id', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
            "_id": lambda n : setattr(self, '_id', n.get_str_value()),
            "_score": lambda n : setattr(self, '_score', n.get_int_value()),
            "_source": lambda n : setattr(self, '_source', n.get_object_value(entity.Entity)),
            "_summary": lambda n : setattr(self, '_summary', n.get_str_value()),
        }
        return fields
    
    @property
    def hit_id(self,) -> Optional[str]:
        """
        Gets the hitId property value. The internal identifier for the item. The format of the identifier varies based on the entity type. For details, see hitId format.
        Returns: Optional[str]
        """
        return self._hit_id
    
    @hit_id.setter
    def hit_id(self,value: Optional[str] = None) -> None:
        """
        Sets the hitId property value. The internal identifier for the item. The format of the identifier varies based on the entity type. For details, see hitId format.
        Args:
            value: Value to set for the hit_id property.
        """
        self._hit_id = value
    
    @property
    def is_collapsed(self,) -> Optional[bool]:
        """
        Gets the isCollapsed property value. Indicates whether the current result is collapses when the collapseProperties property is used.
        Returns: Optional[bool]
        """
        return self._is_collapsed
    
    @is_collapsed.setter
    def is_collapsed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCollapsed property value. Indicates whether the current result is collapses when the collapseProperties property is used.
        Args:
            value: Value to set for the is_collapsed property.
        """
        self._is_collapsed = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def rank(self,) -> Optional[int]:
        """
        Gets the rank property value. The rank or the order of the result.
        Returns: Optional[int]
        """
        return self._rank
    
    @rank.setter
    def rank(self,value: Optional[int] = None) -> None:
        """
        Sets the rank property value. The rank or the order of the result.
        Args:
            value: Value to set for the rank property.
        """
        self._rank = value
    
    @property
    def resource(self,) -> Optional[entity.Entity]:
        """
        Gets the resource property value. The resource property
        Returns: Optional[entity.Entity]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[entity.Entity] = None) -> None:
        """
        Sets the resource property value. The resource property
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def result_template_id(self,) -> Optional[str]:
        """
        Gets the resultTemplateId property value. ID of the result template for rendering the search result. This ID must map to a display layout in the resultTemplates dictionary, included in the searchresponse as well.
        Returns: Optional[str]
        """
        return self._result_template_id
    
    @result_template_id.setter
    def result_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resultTemplateId property value. ID of the result template for rendering the search result. This ID must map to a display layout in the resultTemplates dictionary, included in the searchresponse as well.
        Args:
            value: Value to set for the result_template_id property.
        """
        self._result_template_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("contentSource", self.content_source)
        writer.write_str_value("hitId", self.hit_id)
        writer.write_bool_value("isCollapsed", self.is_collapsed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("rank", self.rank)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resultTemplateId", self.result_template_id)
        writer.write_str_value("summary", self.summary)
        writer.write_str_value("_id", self._id)
        writer.write_int_value("_score", self._score)
        writer.write_object_value("_source", self._source)
        writer.write_str_value("_summary", self._summary)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def summary(self,) -> Optional[str]:
        """
        Gets the summary property value. A summary of the result, if a summary is available.
        Returns: Optional[str]
        """
        return self._summary
    
    @summary.setter
    def summary(self,value: Optional[str] = None) -> None:
        """
        Sets the summary property value. A summary of the result, if a summary is available.
        Args:
            value: Value to set for the summary property.
        """
        self._summary = value
    

