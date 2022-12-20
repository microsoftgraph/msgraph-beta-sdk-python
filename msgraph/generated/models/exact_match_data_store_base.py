from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
exact_data_match_store_column = lazy_import('msgraph.generated.models.exact_data_match_store_column')

class ExactMatchDataStoreBase(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def columns(self,) -> Optional[List[exact_data_match_store_column.ExactDataMatchStoreColumn]]:
        """
        Gets the columns property value. The columns property
        Returns: Optional[List[exact_data_match_store_column.ExactDataMatchStoreColumn]]
        """
        return self._columns
    
    @columns.setter
    def columns(self,value: Optional[List[exact_data_match_store_column.ExactDataMatchStoreColumn]] = None) -> None:
        """
        Sets the columns property value. The columns property
        Args:
            value: Value to set for the columns property.
        """
        self._columns = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new exactMatchDataStoreBase and sets the default values.
        """
        super().__init__()
        # The columns property
        self._columns: Optional[List[exact_data_match_store_column.ExactDataMatchStoreColumn]] = None
        # The dataLastUpdatedDateTime property
        self._data_last_updated_date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchDataStoreBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchDataStoreBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactMatchDataStoreBase()
    
    @property
    def data_last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the dataLastUpdatedDateTime property value. The dataLastUpdatedDateTime property
        Returns: Optional[datetime]
        """
        return self._data_last_updated_date_time
    
    @data_last_updated_date_time.setter
    def data_last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the dataLastUpdatedDateTime property value. The dataLastUpdatedDateTime property
        Args:
            value: Value to set for the dataLastUpdatedDateTime property.
        """
        self._data_last_updated_date_time = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(exact_data_match_store_column.ExactDataMatchStoreColumn)),
            "data_last_updated_date_time": lambda n : setattr(self, 'data_last_updated_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_datetime_value("dataLastUpdatedDateTime", self.data_last_updated_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

