from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class BulkDriverActionResult(AdditionalDataHolder, Parsable):
    """
    A complex type to represent the result of bulk driver action.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new bulkDriverActionResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of driver Ids where the action is failed.
        self._failed_driver_ids: Optional[List[str]] = None
        # List of driver Ids that are not found.
        self._not_found_driver_ids: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # List of driver Ids where the action is successful.
        self._successful_driver_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BulkDriverActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BulkDriverActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BulkDriverActionResult()
    
    @property
    def failed_driver_ids(self,) -> Optional[List[str]]:
        """
        Gets the failedDriverIds property value. List of driver Ids where the action is failed.
        Returns: Optional[List[str]]
        """
        return self._failed_driver_ids
    
    @failed_driver_ids.setter
    def failed_driver_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the failedDriverIds property value. List of driver Ids where the action is failed.
        Args:
            value: Value to set for the failedDriverIds property.
        """
        self._failed_driver_ids = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "failed_driver_ids": lambda n : setattr(self, 'failed_driver_ids', n.get_collection_of_primitive_values(str)),
            "not_found_driver_ids": lambda n : setattr(self, 'not_found_driver_ids', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successful_driver_ids": lambda n : setattr(self, 'successful_driver_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def not_found_driver_ids(self,) -> Optional[List[str]]:
        """
        Gets the notFoundDriverIds property value. List of driver Ids that are not found.
        Returns: Optional[List[str]]
        """
        return self._not_found_driver_ids
    
    @not_found_driver_ids.setter
    def not_found_driver_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notFoundDriverIds property value. List of driver Ids that are not found.
        Args:
            value: Value to set for the notFoundDriverIds property.
        """
        self._not_found_driver_ids = value
    
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
        writer.write_collection_of_primitive_values("failedDriverIds", self.failed_driver_ids)
        writer.write_collection_of_primitive_values("notFoundDriverIds", self.not_found_driver_ids)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("successfulDriverIds", self.successful_driver_ids)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def successful_driver_ids(self,) -> Optional[List[str]]:
        """
        Gets the successfulDriverIds property value. List of driver Ids where the action is successful.
        Returns: Optional[List[str]]
        """
        return self._successful_driver_ids
    
    @successful_driver_ids.setter
    def successful_driver_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the successfulDriverIds property value. List of driver Ids where the action is successful.
        Args:
            value: Value to set for the successfulDriverIds property.
        """
        self._successful_driver_ids = value
    

