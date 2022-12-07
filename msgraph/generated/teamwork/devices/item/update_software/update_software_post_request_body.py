from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_software_type = lazy_import('msgraph.generated.models.teamwork_software_type')

class UpdateSoftwarePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateSoftware method.
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
        Instantiates a new updateSoftwarePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The softwareType property
        self._software_type: Optional[teamwork_software_type.TeamworkSoftwareType] = None
        # The softwareVersion property
        self._software_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateSoftwarePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateSoftwarePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateSoftwarePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "software_type": lambda n : setattr(self, 'software_type', n.get_enum_value(teamwork_software_type.TeamworkSoftwareType)),
            "software_version": lambda n : setattr(self, 'software_version', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("softwareType", self.software_type)
        writer.write_str_value("softwareVersion", self.software_version)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def software_type(self,) -> Optional[teamwork_software_type.TeamworkSoftwareType]:
        """
        Gets the softwareType property value. The softwareType property
        Returns: Optional[teamwork_software_type.TeamworkSoftwareType]
        """
        return self._software_type
    
    @software_type.setter
    def software_type(self,value: Optional[teamwork_software_type.TeamworkSoftwareType] = None) -> None:
        """
        Sets the softwareType property value. The softwareType property
        Args:
            value: Value to set for the softwareType property.
        """
        self._software_type = value
    
    @property
    def software_version(self,) -> Optional[str]:
        """
        Gets the softwareVersion property value. The softwareVersion property
        Returns: Optional[str]
        """
        return self._software_version
    
    @software_version.setter
    def software_version(self,value: Optional[str] = None) -> None:
        """
        Sets the softwareVersion property value. The softwareVersion property
        Args:
            value: Value to set for the softwareVersion property.
        """
        self._software_version = value
    

