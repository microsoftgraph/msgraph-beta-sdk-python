from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_software_freshness = lazy_import('msgraph.generated.models.teamwork_software_freshness')

class TeamworkSoftwareUpdateStatus(AdditionalDataHolder, Parsable):
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
    def available_version(self,) -> Optional[str]:
        """
        Gets the availableVersion property value. The available software version to update.
        Returns: Optional[str]
        """
        return self._available_version
    
    @available_version.setter
    def available_version(self,value: Optional[str] = None) -> None:
        """
        Sets the availableVersion property value. The available software version to update.
        Args:
            value: Value to set for the availableVersion property.
        """
        self._available_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkSoftwareUpdateStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The available software version to update.
        self._available_version: Optional[str] = None
        # The current software version.
        self._current_version: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The update status of the software. The possible values are: unknown, latest, updateAvailable, unknownFutureValue.
        self._software_freshness: Optional[teamwork_software_freshness.TeamworkSoftwareFreshness] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkSoftwareUpdateStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSoftwareUpdateStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkSoftwareUpdateStatus()
    
    @property
    def current_version(self,) -> Optional[str]:
        """
        Gets the currentVersion property value. The current software version.
        Returns: Optional[str]
        """
        return self._current_version
    
    @current_version.setter
    def current_version(self,value: Optional[str] = None) -> None:
        """
        Sets the currentVersion property value. The current software version.
        Args:
            value: Value to set for the currentVersion property.
        """
        self._current_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "available_version": lambda n : setattr(self, 'available_version', n.get_str_value()),
            "current_version": lambda n : setattr(self, 'current_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "software_freshness": lambda n : setattr(self, 'software_freshness', n.get_enum_value(teamwork_software_freshness.TeamworkSoftwareFreshness)),
        }
        return fields
    
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
        writer.write_str_value("availableVersion", self.available_version)
        writer.write_str_value("currentVersion", self.current_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("softwareFreshness", self.software_freshness)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def software_freshness(self,) -> Optional[teamwork_software_freshness.TeamworkSoftwareFreshness]:
        """
        Gets the softwareFreshness property value. The update status of the software. The possible values are: unknown, latest, updateAvailable, unknownFutureValue.
        Returns: Optional[teamwork_software_freshness.TeamworkSoftwareFreshness]
        """
        return self._software_freshness
    
    @software_freshness.setter
    def software_freshness(self,value: Optional[teamwork_software_freshness.TeamworkSoftwareFreshness] = None) -> None:
        """
        Sets the softwareFreshness property value. The update status of the software. The possible values are: unknown, latest, updateAvailable, unknownFutureValue.
        Args:
            value: Value to set for the softwareFreshness property.
        """
        self._software_freshness = value
    

