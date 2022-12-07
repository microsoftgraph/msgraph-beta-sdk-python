from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

quality_update_classification = lazy_import('msgraph.generated.models.windows_updates.quality_update_classification')
windows_update_reference = lazy_import('msgraph.generated.models.windows_updates.windows_update_reference')

class QualityUpdateReference(windows_update_reference.WindowsUpdateReference):
    @property
    def classification(self,) -> Optional[quality_update_classification.QualityUpdateClassification]:
        """
        Gets the classification property value. Specifies the classification of the referenced content. Supports a subset of the values for qualityUpdateClassification. Possible values are: security, unknownFutureValue.
        Returns: Optional[quality_update_classification.QualityUpdateClassification]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[quality_update_classification.QualityUpdateClassification] = None) -> None:
        """
        Sets the classification property value. Specifies the classification of the referenced content. Supports a subset of the values for qualityUpdateClassification. Possible values are: security, unknownFutureValue.
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new QualityUpdateReference and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.qualityUpdateReference"
        # Specifies the classification of the referenced content. Supports a subset of the values for qualityUpdateClassification. Possible values are: security, unknownFutureValue.
        self._classification: Optional[quality_update_classification.QualityUpdateClassification] = None
        # Specifies a quality update in the given servicingChannel with the given classification by date (i.e. the last update published on the specified date). Default value is security.
        self._release_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> QualityUpdateReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: QualityUpdateReference
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return QualityUpdateReference()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(quality_update_classification.QualityUpdateClassification)),
            "release_date_time": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def release_date_time(self,) -> Optional[datetime]:
        """
        Gets the releaseDateTime property value. Specifies a quality update in the given servicingChannel with the given classification by date (i.e. the last update published on the specified date). Default value is security.
        Returns: Optional[datetime]
        """
        return self._release_date_time
    
    @release_date_time.setter
    def release_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the releaseDateTime property value. Specifies a quality update in the given servicingChannel with the given classification by date (i.e. the last update published on the specified date). Default value is security.
        Args:
            value: Value to set for the releaseDateTime property.
        """
        self._release_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("classification", self.classification)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
    

