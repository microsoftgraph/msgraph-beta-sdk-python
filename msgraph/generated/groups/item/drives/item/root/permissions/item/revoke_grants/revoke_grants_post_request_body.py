from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

drive_recipient = lazy_import('msgraph.generated.models.drive_recipient')

class RevokeGrantsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the revokeGrants method.
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
        Instantiates a new revokeGrantsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The grantees property
        self._grantees: Optional[List[drive_recipient.DriveRecipient]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RevokeGrantsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RevokeGrantsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RevokeGrantsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "grantees": lambda n : setattr(self, 'grantees', n.get_collection_of_object_values(drive_recipient.DriveRecipient)),
        }
        return fields
    
    @property
    def grantees(self,) -> Optional[List[drive_recipient.DriveRecipient]]:
        """
        Gets the grantees property value. The grantees property
        Returns: Optional[List[drive_recipient.DriveRecipient]]
        """
        return self._grantees
    
    @grantees.setter
    def grantees(self,value: Optional[List[drive_recipient.DriveRecipient]] = None) -> None:
        """
        Sets the grantees property value. The grantees property
        Args:
            value: Value to set for the grantees property.
        """
        self._grantees = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("grantees", self.grantees)
        writer.write_additional_data_value(self.additional_data)
    

