from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

filter_group = lazy_import('msgraph.generated.models.filter_group')

class Filter(AdditionalDataHolder, Parsable):
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
    def category_filter_groups(self,) -> Optional[List[filter_group.FilterGroup]]:
        """
        Gets the categoryFilterGroups property value. *Experimental* Filter group set used to decide whether given object belongs and should be processed as part of this object mapping. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        Returns: Optional[List[filter_group.FilterGroup]]
        """
        return self._category_filter_groups
    
    @category_filter_groups.setter
    def category_filter_groups(self,value: Optional[List[filter_group.FilterGroup]] = None) -> None:
        """
        Sets the categoryFilterGroups property value. *Experimental* Filter group set used to decide whether given object belongs and should be processed as part of this object mapping. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        Args:
            value: Value to set for the categoryFilterGroups property.
        """
        self._category_filter_groups = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new filter and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # *Experimental* Filter group set used to decide whether given object belongs and should be processed as part of this object mapping. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        self._category_filter_groups: Optional[List[filter_group.FilterGroup]] = None
        # Filter group set used to decide whether given object is in scope for provisioning. This is the filter which should be used in most cases. If an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter is not satisfied any longer, such object will get de-provisioned'. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        self._groups: Optional[List[filter_group.FilterGroup]] = None
        # *Experimental* Filter group set used to filter out objects at the early stage of reading them from the directory. If an object doesn't satisfy this filter it will not be processed further. Important to understand is that if an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter is no longer satisfied, such object will NOT get de-provisioned. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        self._input_filter_groups: Optional[List[filter_group.FilterGroup]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Filter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Filter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Filter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category_filter_groups": lambda n : setattr(self, 'category_filter_groups', n.get_collection_of_object_values(filter_group.FilterGroup)),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(filter_group.FilterGroup)),
            "input_filter_groups": lambda n : setattr(self, 'input_filter_groups', n.get_collection_of_object_values(filter_group.FilterGroup)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def groups(self,) -> Optional[List[filter_group.FilterGroup]]:
        """
        Gets the groups property value. Filter group set used to decide whether given object is in scope for provisioning. This is the filter which should be used in most cases. If an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter is not satisfied any longer, such object will get de-provisioned'. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        Returns: Optional[List[filter_group.FilterGroup]]
        """
        return self._groups
    
    @groups.setter
    def groups(self,value: Optional[List[filter_group.FilterGroup]] = None) -> None:
        """
        Sets the groups property value. Filter group set used to decide whether given object is in scope for provisioning. This is the filter which should be used in most cases. If an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter is not satisfied any longer, such object will get de-provisioned'. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        Args:
            value: Value to set for the groups property.
        """
        self._groups = value
    
    @property
    def input_filter_groups(self,) -> Optional[List[filter_group.FilterGroup]]:
        """
        Gets the inputFilterGroups property value. *Experimental* Filter group set used to filter out objects at the early stage of reading them from the directory. If an object doesn't satisfy this filter it will not be processed further. Important to understand is that if an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter is no longer satisfied, such object will NOT get de-provisioned. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        Returns: Optional[List[filter_group.FilterGroup]]
        """
        return self._input_filter_groups
    
    @input_filter_groups.setter
    def input_filter_groups(self,value: Optional[List[filter_group.FilterGroup]] = None) -> None:
        """
        Sets the inputFilterGroups property value. *Experimental* Filter group set used to filter out objects at the early stage of reading them from the directory. If an object doesn't satisfy this filter it will not be processed further. Important to understand is that if an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter is no longer satisfied, such object will NOT get de-provisioned. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
        Args:
            value: Value to set for the inputFilterGroups property.
        """
        self._input_filter_groups = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("categoryFilterGroups", self.category_filter_groups)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_object_values("inputFilterGroups", self.input_filter_groups)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

